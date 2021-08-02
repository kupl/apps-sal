import math
from decimal import Decimal
n = int(input())
d = [[] for i in range(n)]
for i in range(n):
    d[i] = list(map(Decimal, input().split()))


def cnt(m):
    l = m - 1
    if (l < 0): l = n - 1
    r = (m + 1) % n
    lol = Decimal(2)
    a = ((d[l][0] - d[m][0])**lol + (d[l][1] - d[m][1]) ** 2)**(Decimal(1 / 2))
    b = ((d[m][0] - d[r][0]) ** lol + (d[m][1] - d[r][1]) ** 2)**(Decimal(1 / 2))
    c = ((d[l][0] - d[r][0]) ** lol + (d[l][1] - d[r][1]) ** 2)**(Decimal(1 / 2))
    p = (a + b + c) / lol
    s = (p * (p - a) * (p - b) * (p - c))**(Decimal(1 / 2))
    return Decimal(s / c)


ans = Decimal(cnt(0))
for i in range(0, n):
    ans = min(ans, cnt(i))
    # for j in range(0,n):
    #     if i == j :continue;
    #     cur = ((d[i][0] - d[j][0]) ** 2 + (d[i][1] - d[j][1]) ** 2) ** (1/2)
    #     ans = min(ans, cur / 2)

print(ans)
