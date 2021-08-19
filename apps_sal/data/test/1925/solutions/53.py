(A, B, N) = list(map(int, input().split()))
x = min(B - 1, N)
print(A * x // B - A * int(x // B))
