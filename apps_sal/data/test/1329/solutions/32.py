from itertools import combinations
from collections import defaultdict
n = int(input())


def sieve(n):
    n += 1
    res = [i for i in range(n)]
    for p in range(2, int(n**.5)+1):
        if res[p] < p:
            continue
        for q in range(p**2, n, p):
            if res[q] == q:
                res[q] = p
    return res


U = 100
min_factor = sieve(U)


def prime_factor(n):
    res = defaultdict(int)
    while 1 < n:
        res[min_factor[n]] += 1
        n //= min_factor[n]
    return res


cnt = defaultdict(int)
for i in range(1, n+1):
    for k, v in list(prime_factor(i).items()):
        cnt[k] += v

facts = list(cnt.keys())
ans = 0
# 3,5,5
for subset in combinations(facts, 3):
    for i in range(3):
        can_be = 1
        for j, prim in enumerate(subset):
            if i == j:
                if cnt[prim] < 2:
                    can_be = 0
                    break
            else:
                if cnt[prim] < 4:
                    can_be = 0
                    break
        if can_be:
            ans += 1

# 15,5 3,25
for subset in combinations(facts, 2):
    for i in range(2):
        can_be = 1
        for j, prim in enumerate(subset):
            if i == j:
                if cnt[prim] < 4:
                    can_be = 0
                    break
            else:
                if cnt[prim] < 14:
                    can_be = 0
                    break
        if can_be:
            ans += 1

        can_be2 = 1
        for j, prim in enumerate(subset):
            if i == j:
                if cnt[prim] < 2:
                    can_be2 = 0
                    break
            else:
                if cnt[prim] < 24:
                    can_be2 = 0
                    break
        if can_be2:
            ans += 1

# 74個の場合
if 74 <= cnt[2]:
    ans += 1

print(ans)

