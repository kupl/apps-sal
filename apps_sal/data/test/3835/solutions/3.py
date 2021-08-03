import math
n = int(input())
m = [list(map(int, input().split())) for i in range(n)]


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


g = m[0][1]
for i in range(2, n):
    g = gcd(g, m[0][i])
b = [m[0][i] / g for i in range(1, n)]  # a2, a3,.., an jest wielokrotnoscia b
kw = math.sqrt(m[1][2] / (b[0] * b[1]))
c = [b[i] * kw for i in range(n - 1)]
a0 = m[0][1] / c[0]
c = [a0] + c
for i in c:
    print(int(i), end=" ")
