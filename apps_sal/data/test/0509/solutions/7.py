from itertools import product
N = int(input())
A = [int(input()) for i in range(N)]
for P in product([0, 1], repeat=N):
    d = 0
    for (a, p) in zip(A, P):
        if p:
            d += a
        else:
            d -= a
    if d % 360 == 0:
        print('YES')
        break
else:
    print('NO')
