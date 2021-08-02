H, W, N = [int(v) for v in input().split()]
points = (list(map(int, input().split())) for _ in range(N))
memory = {}
for ai, bi in points:
    for i in range(max(2, ai - 1), min(H - 1, ai + 1) + 1):
        for j in range(max(2, bi - 1), min(W - 1, bi + 1) + 1):
            key = (i, j)
            if not key in memory:
                memory[key] = 0
            memory[key] += 1

counter = {i: 0 for i in range(1, 10)}
for v in list(memory.values()):
    counter[v] += 1

print(((H - 2) * (W - 2) - sum(counter.values())))
for i in range(1, 10):
    print((counter[i]))
