import sys
sys.setrecursionlimit(10 ** 5)
(n, u, v) = list(map(int, input().split()))
u -= 1
v -= 1
m_mat = [[] for i in range(n)]
for _ in range(n - 1):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    m_mat[a].append(b)
    m_mat[b].append(a)
u_map = [-1] * n
v_map = [-1] * n
u_map[u] = 0
v_map[v] = 0


def dfs(current, depth, ma):
    for nex in m_mat[current]:
        if ma[nex] > -1:
            continue
        ma[nex] = depth
        dfs(nex, depth + 1, ma)


dfs(u, 1, u_map)
dfs(v, 1, v_map)
ans = -1
for i in range(n):
    if u_map[i] < v_map[i] and v_map[i] > ans:
        ans = v_map[i]
print(ans - 1)
