(n, m) = map(int, input().split())
p = list([int(s) - 1 for s in input().split()])
nastya = p[-1]
good = [False] * n
swaps = [[] for _ in range(n)]
counts = [0] * n
for _ in range(m):
    (u, v) = map(int, input().split())
    u -= 1
    v -= 1
    if v == nastya:
        good[u] = True
    else:
        swaps[v].append(u)
total = 0
bad_count = 0
for (i, pupil) in enumerate(p[-2::-1]):
    if good[pupil] and counts[pupil] >= bad_count:
        total += 1
    else:
        bad_count += 1
        for u in swaps[pupil]:
            counts[u] += 1
print(total)
