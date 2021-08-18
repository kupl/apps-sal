import math
y, k, n = list(map(int, input().split()))
l = [k * i - y for i in range(math.ceil((y + 1) / k), n // k + 1)]
if len(l) is 0:
    print(-1)
else:
    print(' '.join(map(str, l)))
