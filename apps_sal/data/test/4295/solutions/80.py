(N, K) = list(map(int, input().split()))
if N == K:
    print(0)
elif N < K:
    lis1 = [N, abs(N - K)]
    print(min(lis1))
else:
    lis2 = [N % K, abs(N % K - K)]
    print(min(lis2))
