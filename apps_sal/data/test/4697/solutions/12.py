(N, M) = map(int, input().split())
print(M // 2 if 2 * N > M else N + (M - 2 * N) // 4)
