N, K = map(int, input().split())
print([1, 0][N % K == 0])
