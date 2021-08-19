mod = 10 ** 9 + 7
(N, K) = map(int, input().split())
ans = 1


def main(i):
    m = i * (i - 1) // 2
    M = m + i * (N - i + 1)
    return M - m + 1


for i in range(K, N + 1):
    ans += main(i)
print(ans % mod)
