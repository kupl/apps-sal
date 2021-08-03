from math import floor
A, B, N = map(int, input().split())

if B - 1 <= N:
    x = B - 1
else:
    x = N

print(floor(A * x / B) - A * floor(x / B))
