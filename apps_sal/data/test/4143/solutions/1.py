import math
N = int(input())
p = [0] * 5
bn = float('inf')
for i in range(5):
    p[i] = int(input())
    if bn > p[i]:
        bn = p[i]
ans = 0
print((math.ceil(N / bn) + (5 - 1)))
