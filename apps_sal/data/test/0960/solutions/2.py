n, k = list(map(int, input().split()))
import math
d = k - 1
while n % d != 0:
    d -= 1
print(n // d * k + d)

