(N, X) = map(int, input().split())
x = list(map(int, input().split()))
x = sorted([abs(i - X) for i in x])
y = x[0]
for i in range(1, N):
    z = x[i]
    (y, z) = (max(y, z), min(y, z))
    while z != 0:
        (y, z) = (z, y % z)
print(y)
