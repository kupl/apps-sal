from itertools import product

n = int(input())
data = {}
for p in range(1, n + 1):
    a = int(input())
    data[p] = [list(map(int, input().split())) for _ in range(a)]

ans = 0
for honest in product(range(2), repeat=n):
    for p, hk in enumerate(honest, 1):
        if hk == 1:
            if not all([honest[x - 1] == y for x, y in data[p]]):
                break
    else:
        ans = max(ans, sum(honest))

print(ans)
