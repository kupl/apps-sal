def dfs(v, g, vis):
    count = 1
    first = v
    st = [v]
    vis[v] = True
    while st:
        v = st[-1]
        st.pop()
        if len(g[v]) != 2 or vis[g[v][0]] and vis[g[v][1]] and g[v][0] != first and g[v][1] != first:
            count = 0
        for i in range(len(g[v])):
            if not vis[g[v][i]]:
                vis[g[v][i]] = True
                st.append(g[v][i])
                if v == first and count:
                    break
    if len(g[first]) == 2 and not vis[g[first][1]]:
        st.append(g[first][1])
        while st:
            v = st[-1]
            st.pop()
            for i in range(len(g[v])):
                if not vis[g[v][i]]:
                    vis[g[v][i]] = True
                    st.append(g[v][i])
    return count


v, e = list(map(int, input().split()))
g = [[] for i in range(v)]
for i in range(e):
    f, to = list(map(int, input().split()))
    g[f - 1].append(to - 1)
    g[to - 1].append(f - 1)
vis = [False] * v
ans = 0
for i in range(v):
    if not vis[i]:
        ans += dfs(i, g, vis)
print(ans)
