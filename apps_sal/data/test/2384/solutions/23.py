N = int(input())
A = [int(x) for x in input().split()]

x, y, z = A[0], A[1], 0
for i in range(2, N):
    if i % 2 == 0:
        z = z + A[i]
        y = max(y, x)
        x = x + A[i]
    else:
        z = max(y, z)
        y = y + A[i]
        x = x

if N % 2 == 0:
    print((max(x, y)))
else:
    print((max(y, z)))
