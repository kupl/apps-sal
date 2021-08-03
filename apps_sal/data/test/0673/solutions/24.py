import math

n, k = list(map(int, input().split()))

print((math.floor(n / k) + 1) * k)
