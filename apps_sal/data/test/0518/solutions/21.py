import math
n, r = list(map(int, input().split()))
ang = math.pi * (n - 2) / (2 * n)
print((r * math.cos(ang)) / (1 - math.cos(ang)))
