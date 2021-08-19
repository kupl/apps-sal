(N, K) = map(int, input().split())
A = list(map(int, input().split()))
if N <= K:
    print(1)
elif (N - 1) % (K - 1) == 0:
    print((N - 1) // (K - 1))
else:
    print((N - 1) // (K - 1) + 1)
