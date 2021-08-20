import math
(n, m) = map(int, input().split())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
sum = 0
for i in range(n):
    n = math.sqrt(li[i][0] ** 2 + li[i][1] ** 2)
    if n <= m:
        sum += 1
print(sum)
