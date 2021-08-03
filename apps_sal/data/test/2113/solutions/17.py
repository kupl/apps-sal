n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

st = [(1, 0, 0)]
m = 0
while st:
    u, p, c = st.pop()
    m += c
    st.extend((v, u, 1 - c) for v in g[u] if v != p)

print(m * (n - m) - n + 1)
