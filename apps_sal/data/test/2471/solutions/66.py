from collections import defaultdict
(h, w, n) = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n)]
dct = defaultdict(int)
ans = {i: 0 for i in range(10)}
ans[0] = (h - 2) * (w - 2)
for (a, b) in ab:
    a -= 1
    b -= 1
    u = max(0, a - 2)
    d = min(h - 3, a)
    l = max(0, b - 2)
    r = min(w - 3, b)
    for i in range(u, d + 1):
        for j in range(l, r + 1):
            ans[dct[i, j]] -= 1
            dct[i, j] += 1
            ans[dct[i, j]] += 1
for i in range(10):
    print(ans[i])
