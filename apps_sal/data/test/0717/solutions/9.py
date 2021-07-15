n = int(input())
ans = 0
c = 1
import math
for i in range(n):
    s,d = map(int, input().split())
    p = int(math.ceil(max(0, c - s) / d))
    c = s + p*d + 1
print(c-1)
