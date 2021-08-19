import math
(n, x) = map(int, input().split())
xl = list(map(int, input().split()))
dis = []
ans = 0
for i in range(n):
    dis.append(abs(x - xl[i]))
for i in range(n):
    ans = math.gcd(ans, dis[i])
print(ans)
