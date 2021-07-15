from copy import copy
h, w = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(10)]

c = [list(map(int, input().split())) for _ in range(h)]

d = copy(data)
def cnt_set(d):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
cnt_set(d)
ans = 0

for i in range(h):
    for j in range(w):
        if c[i][j] == -1:
            continue
        ans += d[c[i][j]][1]

print(ans)
