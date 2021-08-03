import math
n = int(input())
a = list(map(int, input().split()))
a = list(reversed(a))
s = 0
m = math.inf
for i in range(len(a)):
    m = min(max(m - 1, 0), a[i])
    s += m
print(s)
