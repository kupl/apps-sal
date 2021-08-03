import math
t = int(input())
for i in range(t):
    a, b, c, d, k = list(map(int, input().split()))
    first = math.ceil(a / c)
    second = math.ceil(b / d)
    if first + second <= k:
        print(first, second)
    else:
        print(-1)
