(h, w, D) = map(int, input().split())
a = []
for _ in range(h):
    b = list(map(int, input().split()))
    a.append(b)
d = {}
for i in range(h):
    c = a[i]
    for j in range(w):
        d[c[j]] = (i + 1, j + 1)
R_min = h * w
R_max = 1
query = []
q = int(input())
for _ in range(q):
    (l, r) = map(int, input().split())
    query.append([l, r])
    R_min = min(l, R_min)
    R_max = max(r, R_max)
cum = [0] * (h * w + 1)
for k in range(R_min, R_max - D + 1):
    prev = cum[k - 1]
    cost = abs(d[k + D][0] - d[k][0]) + abs(d[k + D][1] - d[k][1])
    cum[k + D - 1] = cost + prev
for j in range(q):
    (l, r) = (query[j][0], query[j][1])
    score = cum[r - 1] - cum[l - 1]
    print(score)
