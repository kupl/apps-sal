from functools import reduce
N, M = map(int, input().split())
L = 1 << N
table = {0: 0}
for _ in range(M):
    cost, _ = map(int, input().split())
    match = reduce(lambda a, b: a | b, (1 << shamt for shamt in map(lambda n: int(n) - 1, input().split())))
    for l, now in table.copy().items():
        table[l | match] = min(now + cost, table.get(l | match, 10 ** 7))
print(table[L - 1] if table.get(L - 1, False) else -1)
