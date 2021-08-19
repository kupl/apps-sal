n = int(input())
inp = [int(x) for x in input().split()]
inv = [0 for x in range(0, 147)]
for x in inp:
    for v in range(0, x):
        inv[v] += 1
res = []
for i in range(0, n):
    x = 0
    while inv[x] >= n - i:
        x += 1
    res.append(str(x))
print(' '.join(res))
