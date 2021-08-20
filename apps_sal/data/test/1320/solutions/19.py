import collections
import math
n = int(input())
t = [input() for _ in range(n)]
ans = 0
for i in range(n):
    x = t[i].count('C')
    if x >= 2:
        ans += (x - 1) * x // 2
for i in range(n):
    temp = 0
    for j in range(n):
        if t[j][i] == 'C':
            temp += 1
    if temp >= 2:
        ans += (temp - 1) * temp // 2
print(ans)
