(h, w, d) = map(int, input().split())
xy = [(0, 0)] * (h * w + 1)
for i in range(h):
    a = list(map(int, input().split()))
    for j in range(w):
        xy[a[j]] = (i + 1, j + 1)
s = [0] * (h * w + 1)
for i in range(d + 1, h * w + 1):
    s[i] = abs(xy[i][0] - xy[i - d][0]) + abs(xy[i][1] - xy[i - d][1]) + s[i - d]
q = int(input())
for _ in range(q):
    (l, r) = map(int, input().split())
    print(s[r] - s[l])
