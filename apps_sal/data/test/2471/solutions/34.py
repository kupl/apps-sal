from collections import defaultdict
(H, W, N) = map(int, input().split())
d = defaultdict(int)
ta = [1, 1, 0, -1, -1, -1, 0, 1, 0]
tb = [0, 1, 1, 1, 0, -1, -1, -1, 0]
for _ in range(N):
    (a, b) = map(int, input().split())
    for i in range(9):
        na = a + ta[i]
        nb = b + tb[i]
        if 1 <= na <= H and 1 <= nb <= W:
            d[na, nb] += 1
ans = [0] * 10
for (i, v) in d.items():
    if 2 <= i[0] <= H - 1 and 2 <= i[1] <= W - 1:
        ans[v] += 1
ans[0] = (H - 2) * (W - 2) - sum(ans)
for i in range(10):
    print(ans[i])
