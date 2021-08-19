import math
(n, k) = map(int, input().split())
if n >= k:
    a = 0
    for i in range(1, k):
        a += 0.5 ** math.ceil(math.log2(k / i))
    print((a + n - k + 1) / n)
else:
    a = 0
    for i in range(1, n + 1):
        a += 0.5 ** math.ceil(math.log2(k / i))
    print(a / n)
