n = int(input())
f = []
b = []
for x in range(n):
    (ni, nj) = list(map(int, input().split()))
    f.append([ni, nj])
    b.append([nj, ni])
f.sort()
b.sort()
m1 = f[n - 2][0]
m2 = 1000000000
for i in range(n - 1):
    m2 = min(m2, f[i][1])
ans = m2 - m1
secmin = b[1][0]
maxi = 0
for i in range(1, n):
    maxi = max(maxi, b[i][1])
ans2 = secmin - maxi
p = max(ans, ans2)
if p < 0:
    p = 0
print(p)
