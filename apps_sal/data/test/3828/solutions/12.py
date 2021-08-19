n = int(input())
ps = list(map(int, input().split()))
pos = [0] * n
for (i, p) in enumerate(ps):
    pos[p - 1] = i
used = [False] * n
longest = 0
for v in range(n):
    if used[v]:
        continue
    i = pos[v]
    w = v
    used[w] = True
    while w < n - 1 and pos[w + 1] > i:
        i = pos[w + 1]
        w += 1
        used[w] = True
    longest = max(longest, w - v + 1)
print(n - longest)
