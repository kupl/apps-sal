import math
n, k = map(int, input().split())
num = 0
for i in range(1, n + 1):
    if i >= k:
        num += 1 / n
    else:
        num += (1 / (n * (2 ** math.ceil(math.log(k / i, 2)))))
print(num)
