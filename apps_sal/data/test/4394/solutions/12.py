import sys
# 26
def input(): return sys.stdin.readline().strip()


ipnut = input


def find(a):
    st = []
    while a != dsu[a]:
        st.append(a)
        a = dsu[a]
    for j in st:
        dsu[j] = a
    return a


def union(a, b, f):
    a = find(a)
    b = find(b)
    if f:
        dsu[a] = b
    else:
        dsu[b] = a


n, m = map(int, input().split())
if m == 0:
    print(0)
    return
dsu = [i for i in range(n)]
h = []
for i in range(m):
    a, b, c = map(int, ipnut().split())
    h.append((c, a - 1, b - 1))
h.sort()
lc = 0
ans = 0
heh = [[h[0]]]
for i in h[1:]:
    if heh[-1][0][0] == i[0]:
        heh[-1].append(i)
    else:
        heh.append([i])
ab = []
for h in heh:
    lol = []
    for c, a, b in h:
        if find(a) != find(b):
            lol.append((a, b))
    for a, b in lol:
        if find(a) == find(b):
            ans += 1
        else:
            union(a, b, ans % 2)
print(ans)
