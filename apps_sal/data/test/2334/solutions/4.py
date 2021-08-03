import math
n = int(input())
a = list(map(int, input().split()))
s = 0
m, f = map(int, input().split())
for i in a:
    if i > m:
        s += math.ceil((i - m) / (f + m)) * f
print(s)
