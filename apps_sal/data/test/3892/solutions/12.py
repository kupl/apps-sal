import copy

n, m = list(map(int, input().strip().split()))
items = [[] for _ in range(n)]
for _ in range(m):
    u, v = list(map(int, input().strip().split()))
    items[u - 1].append(v - 1)
for i, line in enumerate(items):
    pairs = []
    for v in line:
        pairs.append((v - i, v) if v > i else (n - i + v, v))
    pairs = sorted(pairs, reverse=True)
    items[i] = [pair[1] for pair in pairs]
ans = []
for s in range(n):
    need = m
    items_idx = [0 for _ in range(n)]
    items_cnt = [0 for _ in range(n)]
    items_tot = 0
    ans.append(-1)
    while need > 0 or items_tot > 0:
        idx = s % n
        if items_idx[idx] < len(items[idx]):
            items_cnt[items[idx][items_idx[idx]]] += 1
            items_idx[idx] += 1
            items_tot += 1
            need -= 1
        items_tot -= items_cnt[idx]
        items_cnt[idx] = 0
        s += 1
        ans[-1] += 1
    ans[-1] = max(0, ans[-1])
print(' '.join(map(str, ans)))
