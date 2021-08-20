import sys
p = 998244353
n = int(sys.stdin.readline().strip())
A = [0] * (10 ** 6 + 1)
a = []
k = []
for i in range(0, n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    k.append(line[0])
    a.append(line[1:])
    for j in range(0, k[i]):
        x = a[i][j]
        A[x] = A[x] + 1
(r, s) = (0, 1)
for i in range(0, n):
    x = 0
    for j in range(0, k[i]):
        x = x + A[a[i][j]]
    y = k[i] * n
    (r, s) = ((r * y + s * x) % p, s * y % p)
ans = r
s = s * n
q = p - 2
while q > 0:
    if q % 2 == 1:
        ans = ans * s % p
        q = q - 1
    else:
        q = q // 2
        s = s * s % p
print(ans % p)
