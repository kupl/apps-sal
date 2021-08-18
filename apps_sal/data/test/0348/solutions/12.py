import sys
input = sys.stdin.readline
MOD = 998244353

n, m, l, r = map(int, input().split())
h = r - l + 1

s = n * m
if s % 2 == 1:
    ans = pow(h, s, MOD)
    print(ans)
else:
    ans = pow(h, s, MOD)
    if h % 2 == 1:
        ans += 1
    ans *= pow(2, MOD - 2, MOD)
    ans %= MOD
    print(ans)
