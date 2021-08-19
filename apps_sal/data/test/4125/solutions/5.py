import math
(n, x) = map(int, input().split())
xlist = list(map(int, input().split()))
ylist = []
for i in range(n):
    ylist.append(xlist[i] - x)
ans = ylist[0]
for i in range(n):
    ans = math.gcd(ans, ylist[i])
print(ans)
