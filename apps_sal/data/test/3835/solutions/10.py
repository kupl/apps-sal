from math import sqrt
n = int(input())
m = []
for i in range(n):
    s = list(map(int, input().split()))
    m.append(s)
a = []
s = m[0][1] * m[0][2] * m[1][2]
s = int(sqrt(s) + 0.0001)
a1 = s // m[1][2]
a2 = s // m[0][2]
a3 = s // m[0][1]
a = [a1, a2, a3]
for i in range(3, n):
    z = m[0][i] // a1
    a.append(z)
print(*a)
