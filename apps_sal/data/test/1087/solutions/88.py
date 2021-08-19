import sys
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
d = {j: 0 for j in range(41)}
for ai in a:
    for j in range(41):
        if ai >> j & 1:
            d[j] += 1
ans = 0
l = len(bin(k)) - 3
sys.setrecursionlimit(10 ** 7)


def dp(m, t):
    if m < 0:
        return 0
    ret = 0
    if t == 1:
        for i in range(m + 1):
            tmp = max(0, n - 2 * d[i])
            ret += pow(2, i) * tmp
    elif k >> m & 1:
        tmp1 = dp(m - 1, 0) + (n - 2 * d[m]) * pow(2, m)
        tmp0 = dp(m - 1, 1)
        ret += max(tmp1, tmp0)
    else:
        ret += dp(m - 1, 0)
    return ret


print(sum(a) + dp(l, 0))
