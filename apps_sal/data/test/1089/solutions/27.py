
def combination(n, r, mod=10**9 + 7):
    n1, r = n + 1, min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod


def main():
    N, M, K = list(map(int, input().split()))
    mod = 10**9 + 7
    ans1 = 0
    for h in range(1, N):
        ans1 += (N - h) * h
    ans1 = ans1 * M * M % mod
    ans2 = 0
    for w in range(1, M):
        ans2 += (M - w) * w
    ans2 = ans2 * N * N % mod
    ans = (ans1 + ans2) * combination(N * M - 2, K - 2) % mod
    print(ans)


main()
