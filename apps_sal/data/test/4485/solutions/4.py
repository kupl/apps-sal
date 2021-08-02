import collections as c
n, m = map(int, input().split())
print(['POSSIBLE', 'IMPOSSIBLE'][not [1 for c in c.Counter([[a, b][a == 1] for a, b in [[i, j] for i, j in [list(map(int, input().split())) for _ in range(m)] if i == 1 or j == n]]).values() if c > 1]])
