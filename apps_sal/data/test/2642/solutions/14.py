import math
from collections import deque
N = int(input())
a = []
b = []
for i in range(N):
    (i1, i2) = list(map(int, input().split()))
    g = math.gcd(i1, i2)
    if g == 0:
        a.append(i1)
        b.append(i2)
        continue
    x = i1 // g
    y = i2 // g
    if x < 0:
        x = -x
        y = -y
    a.append(x)
    b.append(y)
P = {}
for i in range(N):
    if b[i] < 0:
        tmp = b[i]
        b[i] = a[i]
        a[i] = -tmp
        sgn = 1
    elif a[i] == 0 and b[i] != 0:
        a[i] = b[i]
        b[i] = 0
        sgn = 1
    else:
        sgn = 0
    if (a[i], b[i]) in P:
        P[a[i], b[i]][sgn] = P[a[i], b[i]][sgn] + 1
    elif sgn == 0:
        P[a[i], b[i]] = [1, 0]
    else:
        P[a[i], b[i]] = [0, 1]
MOD = 1000000007
a1 = 1
ans0 = 0
for k in P:
    if k == (0, 0):
        ans0 = P[k][0]
    else:
        a1 = a1 * (pow(2, P[k][0], MOD) + pow(2, P[k][1], MOD) - 1) % MOD
if ans0 != 0:
    ans = ans0 + a1 - 1
else:
    ans = a1 - 1
print(ans % MOD)
