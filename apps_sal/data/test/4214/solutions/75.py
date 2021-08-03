import math
n = int(input())
a = []
b = []
ans = 0


def z(p, q, r, s):
    return ((p - r)**2 + (q - s)**2)**0.5


for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
for i in range(n):
    for j in range(i + 1, n):
        ans += 2 * z(a[i], b[i], a[j], b[j])
ans /= n
print(ans)
