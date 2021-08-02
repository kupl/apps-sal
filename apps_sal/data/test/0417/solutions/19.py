from fractions import gcd
from itertools import accumulate

n, x, d = list(map(int, input().split()))

if d == 0:
    if x == 0:
        print((1))
    else:
        print((n + 1))
    return
elif d < 0:
    x, d = -x, -d

g = gcd(x, d)
back_k = d // g
offset = x // g

lowers = [0] + list(accumulate(list(range(n))))
uppers = [0] + list(accumulate(list(range(n - 1, -1, -1))))
min_memo = [10 ** 18] * min(n + 1, back_k)
max_memo = [-(10 ** 18)] * min(n + 1, back_k)


ans = 0
for k in range(n + 1):
    min_acc = lowers[k]
    max_acc = uppers[k]

    if k < back_k:
        min_memo[k] = min_acc - offset
        max_memo[k] = max_acc - offset
        ans += max_acc - min_acc + 1

        continue

    kk = k % back_k
    back_min = min_memo[kk]
    back_max = max_memo[kk]

    if back_max < min_acc or max_acc < back_min:
        min_memo[kk] = min_acc - offset
        max_memo[kk] = max_acc - offset
        ans += max_acc - min_acc + 1
    else:
        current = max_acc - min_acc + 1
        duplicated = min(max_acc, back_max) - max(min_acc, back_min) + 1
        ans += current - duplicated
        min_memo[kk] = min(min_acc, back_min) - offset
        max_memo[kk] = max(max_acc, back_max) - offset


print(ans)
