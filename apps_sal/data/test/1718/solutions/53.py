import math

n, k = map(int, input().split())
Ai = list(map(int, input().split()))

print(math.ceil((n - k) / (k - 1) + 1))
