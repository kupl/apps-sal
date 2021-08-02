from math import ceil

n, k = list(map(int, input().strip().split()))
r = 2 * n
g = 5 * n
b = 8 * n

print(ceil(r / k) + ceil(g / k) + ceil(b / k))
