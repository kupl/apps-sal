import math
input()
a = list(map(int, input().split()))
(x, y) = list(map(int, input().split()))
s = 0
for i in a:
    if i > x:
        s += math.ceil((i - x) / (x + y))
print(int(s * y))
