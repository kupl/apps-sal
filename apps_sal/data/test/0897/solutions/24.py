import sys
input = sys.stdin.readline
mod = 10 ** 9 + 7


def invmod(x, mod):
    return pow(x, mod - 2, mod)


(n, m) = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    if a[i] == 0 and b[i] == 0:
        (sp, sq) = (m * m, m)
        (tp, tq) = (m * m, m * (m - 1) // 2)
    elif a[i] == 0:
        (sp, sq) = (m, 1)
        (tp, tq) = (m, m - b[i])
    elif b[i] == 0:
        (sp, sq) = (m, 1)
        (tp, tq) = (m, a[i] - 1)
    else:
        (sp, sq) = (1, 1 if a[i] == b[i] else 0)
        (tp, tq) = (1, 1 if a[i] > b[i] else 0)
    dp[i] = sq * invmod(sp, mod) * dp[i + 1]
    dp[i] += tq * invmod(tp, mod)
    dp[i] %= mod
ans = dp[0]
print(ans)
