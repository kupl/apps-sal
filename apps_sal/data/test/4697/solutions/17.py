N, M = map(int, input().split())
M //= 2
print(min(M, (N + M) // 2))
