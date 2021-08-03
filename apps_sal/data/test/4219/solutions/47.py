from itertools import product

n = int(input())
info = {}
for p in range(n):
    a = int(input())
    L = []
    for _ in range(a):
        x, y = list(map(int, input().split()))
        x, y = x - 1, y
        L.append((x, y))
    info[p] = L

ans = 0
for bit_pattern in product(range(2), repeat=n):
    for p, bit in enumerate(bit_pattern):
        if bit:
            if not all([bit_pattern[x] == y for x, y in info[p]]):
                break
    else:
        ans = max(ans, sum(bit_pattern))

print(ans)
