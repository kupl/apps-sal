import math
(n, k) = map(int, input().split())
c = 0
for i in range(1, n + 1):
    if k // i == 0:
        c += 1 / n
    else:
        t = math.ceil(math.log2(k / i))
        c += 0.5 ** t / n
print(c)
