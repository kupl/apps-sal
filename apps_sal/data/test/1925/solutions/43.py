
A, B, N = map(int, input().split())


x = 0
if N >= B:
    x = B - 1
else:
    x = N

print(int(A * x / B))
