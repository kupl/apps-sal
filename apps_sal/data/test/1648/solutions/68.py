N, K = map(int, input().split())
Bp = 1
Rp = N - K + 1

for k in range(K):
    print(Bp * Rp % (10**9 + 7))
    Bp = Bp * (K - k - 1) // (k + 1)
    Rp = Rp * (N - K - k) // (k + 2)
