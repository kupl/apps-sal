import math
n = int(input())
(d, x) = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
count = 0
for num in a:
    count += math.ceil(d / num)
print(count + x)
