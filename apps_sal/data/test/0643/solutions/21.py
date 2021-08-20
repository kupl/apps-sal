import math
for _ in range(int(input())):
    (x, y, p, q) = list(map(int, input().split()))
    if p == 0 or p == q:
        print(0 if x * q == p * y else -1)
        continue
    n = math.ceil((y - x) / (q - p))
    n = max(n, math.ceil(x / p))
    n = max(n, math.ceil(y / q))
    print(n * q - y)
