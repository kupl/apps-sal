import math


k, n, s, p = [int(x) for x in input().strip().split(" ")]

nospp = math.ceil(n / s)
ts = k * nospp
print(math.ceil(ts / p))
