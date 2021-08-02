N, K, T = list(map(int, input().split()))

if T < K:
    print(T)
elif N < T:
    print(N + K - T)
else:
    print(K)
