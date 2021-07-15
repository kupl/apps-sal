n, m = list(map(int, input().split()))
A = [0] * n
z = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    z += a
    A[i] = b - a
A.sort()
k = 0
for i in range(n):
    if z <= m:
        break
    k += 1
    z += A[i]
if z <= m:
    print(k)
else:
    print(-1)

