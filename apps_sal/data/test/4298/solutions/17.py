import math
n, k = list(map(int, input().split()))
print(math.ceil(n / (2 * k + 1)))
