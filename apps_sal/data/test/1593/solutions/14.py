import math
R = lambda: list(map(int, input().split()))
n, sum = R()
x = []; y = []; z = []; dis = []
for i in range(n):
    a, b, c = R()
    x.append(a)
    y.append(b)
    z.append(c)
    dis.append((math.sqrt(a**2 + b ** 2), i))
dis.sort()
i = 0
while sum < 1000000 and i < n:
    sum += z[dis[i][1]]
    i += 1
if sum < 1000000: print('-1')
else: print(dis[i-1][0])

