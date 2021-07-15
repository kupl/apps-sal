mod = 10 ** 9 + 7
N, K = map(int, input().split())

ans = 0
memo = [0] * (K + 1)
for i in range(K, 0, -1):
    x = K // i
    cnt = pow(x, N, mod)

    a = i
    while a <= K:
        cnt -= memo[a]
        a += i

    memo[i] = cnt
    ans += i * cnt
    ans %= mod

print(ans)
