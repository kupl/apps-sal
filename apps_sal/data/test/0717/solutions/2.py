import math
n = int(input())
current_day = 0
for i in range(0, n):
    current_day = current_day + 1
    (s, d) = [int(x) for x in input().split(' ')]
    p = max(0, math.ceil((current_day - s) / d))
    current_day = s + p * d
print(current_day)
