A, B, N = list(map(int, input().split()))
print(((A * min(N, B - 1)) // B))
