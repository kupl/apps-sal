import sys
read = lambda: list(map(int, sys.stdin.readline().split()))
n, m, k = read()

table = []
for _ in range(n):
    table.append(read())
table = list(zip(*table))

locked_cells = set()
locked_procs = set()
lock_time = [0] * n
for t, ys in enumerate(table):
    cnt = [0] * (k + 1)
    for i, c in enumerate(ys):
        if i not in locked_procs:
            cnt[c] += 1
    for c, cn in enumerate(cnt):
        if c > 0 and cn > 1:
            locked_cells.add(c)
    for i, c in enumerate(ys):
        if c in locked_cells and i not in locked_procs:
            locked_procs.add(i)
            lock_time[i] = t + 1

for t in lock_time:
    print(t)
