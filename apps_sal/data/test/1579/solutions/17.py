import sys
input = sys.stdin.readline
M = 10 ** 5
n = int(input())
G = [[] for _ in range(2 * M + 1)]
for _ in range(n):
    (x, y) = map(int, input().split())
    G[x].append(y + M)
    G[y + M].append(x)
seen = [False] * (2 * M + 1)


def dfs(v):
    stack = [v]
    seen[v] = True
    (cnt_x, cnt_y) = (0, 0)
    while stack:
        v = stack.pop()
        if v <= M:
            cnt_x += 1
        else:
            cnt_y += 1
        for nv in G[v]:
            if seen[nv]:
                continue
            seen[nv] = True
            stack.append(nv)
    return cnt_x * cnt_y


ans = 0
for i in range(2 * M + 1):
    if not seen[i]:
        ans += dfs(i)
ans -= n
print(ans)
