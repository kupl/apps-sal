(N, M) = map(int, input().split())
print(min(N, M // 2) + max(M - N * 2, 0) // 4)
