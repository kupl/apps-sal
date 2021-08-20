(A, B, N) = map(int, input().split())
min = N
if N > B - 1:
    min = B - 1
print(A * min // B - A * (min // B))
