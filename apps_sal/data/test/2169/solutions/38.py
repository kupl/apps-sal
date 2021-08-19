import sys
read = sys.stdin.buffer.read
inp = iter(map(int, read().split()))
(H, W, D) = (next(inp), next(inp), next(inp))
addr = [None] * (H * W + 1)
for i in range(H):
    for j in range(W):
        v = next(inp)
        addr[v] = (i, j)
cost = []
for m in range(D):
    arr = [0]
    for x in range((H * W - m) // D):
        if m + x * D == 0:
            arr.append(0)
            continue
        (r, c) = addr[m + x * D]
        (nr, nc) = addr[m + (x + 1) * D]
        arr.append(arr[-1] + abs(nr - r) + abs(nc - c))
    cost.append(arr)
Q = next(inp)
for _ in range(Q):
    (s, t) = (next(inp), next(inp))
    m = s % D
    ans = cost[m][t // D] - cost[m][s // D]
    print(ans)
