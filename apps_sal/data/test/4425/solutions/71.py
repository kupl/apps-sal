from math import log2, ceil
N, K = map(int, input().split())

p = 0

for i in range(1, N + 1):
    if K >= i:
        p += 2**-(ceil(log2(K / i))) / N
    else:
        p += 1 / N

print(p)
