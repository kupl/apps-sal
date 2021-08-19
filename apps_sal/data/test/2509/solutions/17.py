import math
(n, k) = map(int, input().split())
sum = 0
if k == 0:
    print(n ** 2)
else:
    for b in range(1, n + 1):
        if n % b == 0:
            sum += math.floor(n / b) * max(b - k, 0)
        else:
            sum += math.floor(n / b) * max(b - k, 0) + max(n % b - k + 1, 0)
    print(sum)
