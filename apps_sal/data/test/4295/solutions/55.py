N, K = list(map(int, input().split()))

if N > K:
    N %= K

if (K / 2) >= N:
    print(N)
else:
    print(K - N)
