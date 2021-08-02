h, w, d = map(int, input().split())
g = [[] for _ in range(w)]
for _ in range(h):
    tmp_list = list(map(int, input().split()))
    for i in range(w):
        g[i].append(tmp_list[i])
q = int(input())
qs = [list(map(int, input().split())) for _ in range(q)]
loc = [0] * (h * w + 1)
for i in range(h):
    for j in range(w):
        loc[g[j][i]] = (i, j)
roots = [0] * (h * w + 1)
for i in range(1, d + 1):
    j = i + d
    while j < h * w + 1:
        cost = abs(loc[j][0] - loc[j - d][0]) + abs(loc[j][1] - loc[j - d][1])
        roots[j] = cost + roots[j - d]
        j += d
for i in qs:
    l, r = i[0], i[1]
    print(roots[r] - roots[l])
