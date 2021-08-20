(h, w, d) = map(int, input().split())
loc = [[] for _ in range(w * h + 1)]
cost = [0] * (w * h + 1)
for i in range(h):
    l = list(map(int, input().split()))
    for j in range(w):
        loc[l[j]] = [i, j]
for t in range(w * h + 1, 0, -1):
    if t + d < w * h + 1:
        (ti, tj) = loc[t + d]
        (fi, fj) = loc[t]
        tempcost = abs(fi - ti) + abs(fj - tj)
        cost[t] = cost[t + d] + tempcost
q = int(input())
for i in range(q):
    (l, r) = map(int, input().split())
    print(cost[l] - cost[r])
