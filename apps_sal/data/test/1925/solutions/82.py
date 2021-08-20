(A, B, N) = map(int, input().split())
if N >= B:
    print(A * (B - 1) // B)
else:
    print(A * N // B - A * (N // B))
