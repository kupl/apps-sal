(n, m) = [int(_) for _ in input().split()]
d = [[] for k in range(m + 1)]
for _ in range(n):
    (s, r) = [int(_) for _ in input().split()]
    d[s].append(r)
max_num = 0
for v in d:
    max_num = max(max_num, len(v))
sums = [0] * max_num
for (i, v) in enumerate(d):
    v.sort(reverse=True)
    s = 0
    for (k, j) in enumerate(v):
        s += j
        if s > 0:
            sums[k] += s
        else:
            break
print(max(sums))
