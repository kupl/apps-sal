from sys import stdin

n, m, h = list(map(int, stdin.readline().split()))

cols = list(map(int, stdin.readline().split()))
rows = list(map(int, stdin.readline().split()))

top = [list(map(int, stdin.readline().split())) for i in range(n)]

ans = [[0 if top[i][f] == 0 else min(rows[i], cols[f]) for f in range(m)] for i in range(n)]
print('\n'.join([' '.join(map(str, r)) for r in ans]))
