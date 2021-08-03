from collections import Counter
from itertools import combinations, permutations


def factor(n):
    res = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            res.append(i)
            n //= i
    if n > 1:
        return res + [n]
    else:
        return res


N = int(input())
if N < 10:
    print((0))
    return

cnt = Counter()
for i in range(2, N + 1):
    primes = factor(i)
    cnt += Counter(primes)

ans = 0
for x, y in combinations(cnt, 2):
    if cnt[x] < 4 or cnt[y] < 4:
        continue
    for z in cnt:
        if z == x or z == y or cnt[z] < 2:
            continue
        ans += 1

for x, y in permutations(cnt, 2):
    if cnt[x] >= 14 and cnt[y] >= 4:
        ans += 1

for x, y in permutations(cnt, 2):
    if cnt[x] >= 24 and cnt[y] >= 2:
        ans += 1

for x in cnt:
    if cnt[x] >= 74:
        ans += 1

print(ans)
