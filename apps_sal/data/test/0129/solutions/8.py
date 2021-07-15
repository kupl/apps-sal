N, M, K, L = map(int, input().split())
if N < M or K + L > N:
    print(-1)
else:
    print((L + K - 1) // M + 1 if ((L + K - 1) // M + 1) * M <= N else -1)
