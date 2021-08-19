(N, K) = map(int, input().split())
if N >= K:
    print(min(N % K, K - N % K))
else:
    print(min(N, K - N))
