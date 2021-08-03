import math
n, k = tuple(map(int, input().strip().split(" ")))
numbers = tuple(map(int, input().strip().split(" ")))
l = []
for i in range(k):
    l.append(0)
for i in numbers:
    l[i % k] += 1
s = (l[0] // 2) * 2
for g in range(1, math.ceil(k / 2)):
    s = s + (min(l[g], l[k - g]) * 2)
if(k % 2 == 0):
    s = s + ((l[k // 2] // 2) * 2)
print(s)
