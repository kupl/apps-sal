import math


class circ:

    def __init__(self, x, y, r):
        self.x = x * 1.0
        self.y = y * 1.0
        self.r = r * 1.0


n = 0
n = int(input())
vec = []
for i in range(n):
    st = input().split(' ')
    a = int(st[0])
    b = int(st[1])
    c = int(st[2])
    vec.append(circ(a, b, c))
gr = [[] for i in range(n)]
pad = [-1 for i in range(n)]
vis = [False for i in range(n)]
for i in range(n):
    for k in range(n):
        if i == k:
            continue
        dist = math.hypot(vec[i].x - vec[k].x, vec[i].y - vec[k].y)
        if dist < vec[k].r and vec[k].r > vec[i].r and (pad[i] < 0 or vec[k].r < vec[pad[i]].r):
            pad[i] = k
for i in range(n):
    if pad[i] < 0:
        continue
    gr[pad[i]].append(i)
st = []
ans = 0.0
for i in range(n):
    if pad[i] >= 0 or vis[i]:
        continue
    st.append((i, 0))
    while len(st) > 0:
        (node, level) = st.pop()
        vis[node] = True
        mult = -1.0
        if level == 0 or level % 2 == 1:
            mult = 1.0
        ans += mult * (vec[node].r * vec[node].r * math.pi)
        for next in gr[node]:
            st.append((next, level + 1))
print(ans)
