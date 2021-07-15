def grundy(N, K):
    if N < K:
        return 0
    while N % K:
        hi = N / (N / K + 1) 
        lo = 1
        while hi - lo > 1:
            mid = (hi + lo) / 2
            M = N - mid * (N/ K + 1)
            if M / K == N / K:
                lo = mid
            else:
                hi = mid
        m = N / K + 1
        N -= m * lo
    return N / K

N = input()
ans = 0
for i in range(N):
    a, k = list(map(int, input().split()))
    ans ^= grundy(a, k)
print("Takahashi" if ans else "Aoki")

