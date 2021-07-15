import math

k, n, s, p = list(map(int, input().split()))

print(math.ceil((k * math.ceil(n / s)) / p))

