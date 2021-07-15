read = lambda: list(map(int, input().split()))
n = int(input())
a = [0] + list(read())
g = [list() for i in range(n + 1)]
for i in range(2, n + 1):
    p, c = read()
    g[i].append((p, c))
    g[p].append((i, c))
was = [0] * (n + 1)
st = [(1, 0, 0)]
while st:
    v, mind, dist = st.pop()
    was[v] = 1
    for u, c in g[v]:
        if not was[u]:
            if dist + c - min(dist + c, mind) <= a[u]:
                st.append((u, min(mind, dist + c), dist + c))

ans = n - was.count(1)
print(ans)

