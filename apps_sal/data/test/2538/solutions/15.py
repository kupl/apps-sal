import math
n = int(input())
for i in range(n):
    a, b, c = [int(item) for item in input().split()]
    ans = min(c+1, max(0, math.ceil(((a - b) + c) / 2)))
    print(ans)
