N, K = list(map(int, input().split()))
MOD = 10**9 + 7
memo = {}


def a(n):
    if n in memo:
        return memo[n]
    else:
        ret = pow(n, N, MOD)
        for i in range(2, n+1):
            ret -= a(n//i)
        memo[n] = ret
        return ret


ans = 0
for i in range(1, K+1):
    ans += i*a(K//i)
    ans %= MOD
print(ans)

