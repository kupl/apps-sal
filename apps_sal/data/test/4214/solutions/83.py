n = int(input())
x_y = [ list(map(int, input().split())) for _ in range(n)  ]
import math
d = []
for i in range(n):
    for j in range(n):
        if i != j:
            x1, y1 = x_y[i]
            x2, y2 = x_y[j]
            d.append(math.sqrt((x1-x2)**2+(y1-y2)**2))
print(sum(d)/n)
