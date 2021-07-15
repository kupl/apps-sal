h, w, n, *a = map(int, open(0).read().split())
l = []
for c, a in enumerate(a, 1):
    l += [c] * a
for p in range(h):
    print(*l[p*w:-~p*w][::[1, -1][p%2]])
