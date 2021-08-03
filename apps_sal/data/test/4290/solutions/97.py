N, M = map(int, input().split())
ans = (N + M) * (N + M - 1) // 2 - (N * M)
print(ans)
