__author__ = 'dwliv_000'
(n, m) = (int(i) for i in input().split())
c = [int(i) % m for i in input().split()]
z = [False] * m
for j in c:
    q = z[:]
    q[j] = True
    for i in range(m):
        if(z[i]):
            q[(i + j) % m] = True
    z = q[:]
    if z[0]:
        print('YES')
        return
print('NO')
