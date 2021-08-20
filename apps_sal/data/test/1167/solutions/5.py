import math
amount = int(input())
for i in range(amount):
    (a, b, c, d, k) = [int(s) for s in input().split()]
    if math.ceil(a / c) + math.ceil(b / d) > k:
        print(-1)
    else:
        print(math.ceil(a / c), math.ceil(b / d))
