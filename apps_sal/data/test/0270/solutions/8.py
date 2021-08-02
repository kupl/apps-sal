import numpy as np

n, m = list(map(int, input().split()))
adj = np.zeros((n, n), dtype=np.bool)
for _ in range(m):
    s, t = list(map(int, input().split()))
    adj[s - 1, t - 1] = True
deg = adj.sum(axis=1)

ev = np.zeros(n, dtype=np.float)
for i in range(n - 2, -1, -1):
    ev[i] = ev[adj[i]].mean() + 1.

prob = np.zeros(n, dtype=np.float)
prob[0] = 1.
for i in range(n - 1):
    prob[adj[i]] += prob[i] / deg[i]

decrease = 0.
for i in np.where(deg > 1)[0]:
    now = ev[adj[i]].mean()
    cut = (ev[adj[i]].sum() - ev[adj[i]].max()) / (deg[i] - 1)
    decrease = np.maximum(decrease, (now - cut) * prob[i])

print((ev[0] - decrease))
