import math
n = int(input())
dots = []
for i in range(n):
    temp = list(map(int, input().split()))
    dots.append(temp)
lines = {}
for i in range(n):
    for j in range(i + 1, n):
        dx = dots[i][0] - dots[j][0]
        dy = dots[i][1] - dots[j][1]
        if dx < 0:
            dx = -dx
            dy = -dy
        if dx == 0 and dy < 0:
            dy = -dy
        if (dx, dy) in lines:
            lines[dx, dy] += 1
        else:
            lines[dx, dy] = 1
ans = 0
for x in lines:
    t = lines[x]
    ans += t * (t - 1) / 2
ans /= 2
print(int(ans))
