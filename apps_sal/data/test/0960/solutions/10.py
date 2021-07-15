from math import sqrt

n, k = map(int, input().split())

x = float("inf")

max_div = int(sqrt(n))
for div in range(1, max_div + 1):
    if n % div == 0:
        div2 = n // div
        if div2 < k:
            x = min(x, div * k + div2)
        if div < k:
            x = min(x, div2 * k + div)
print(x)
