import collections as cc
import sys
def I(): return list(map(int, input().split()))


n, = I()
g = cc.defaultdict(list)
for i in range(n - 1):
    x, y = I()
    g[x].append(y)
    g[y].append(x)
col = [-1] * (n + 1)
b = 0
w = 0
visi = [0] * (n + 1)
st = cc.deque()
st.append(1)
col[1] = 1
w += 1
while st:
    x = st.pop()
    visi[x] = 1
    for y in g[x]:
        if not visi[y]:
            col[y] = col[x] ^ 1
            st.append(y)
b = col.count(1)
w = col.count(0)
print(min(b, w) - 1)
