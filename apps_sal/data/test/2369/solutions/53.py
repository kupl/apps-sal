(N, K) = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
mod = 10 ** 9 + 7
fan = [1] * (N + 1)
for i in range(2, N):
    fan[i] = fan[i - 1] * i % mod
ans = 0


def comb(a, b):
    return fan[a] * pow(fan[b], mod - 2, mod) * pow(fan[a - b], mod - 2, mod)


for i in range(N - K + 1):
    ans += comb(N - i - 1, K - 1) * (A[N - i - 1] - A[i])
    ans %= mod
print(ans)
