N, M = [int(x) for x in input().split()]
MOD = 10**9 + 7

if max(N, M) - min(N, M) > 1:
    print((0))
    return


def floor(n):
    result = n
    for i in range(n - 1, 0, -1):
        result *= i
        result %= MOD

    return result


r = floor(max(N, M))
t = floor(min(N, M))

if r == t:
    result = (r * t * 2) % MOD
else:
    result = (r * t) % MOD

print(result)
