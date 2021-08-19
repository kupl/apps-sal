def dfs(pi):
    if len(pi) == n:
        p.append(pi)
        return
    for i in range(1, n + 1):
        if i in pi:
            continue
        cpi = pi + (i,)
        dfs(cpi)


n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
p = []
dfs(tuple())
i = 0
for v in range(len(p)):
    i += 1
    if p[v] == P:
        a = i
    if p[v] == Q:
        b = i
print(abs(a - b))
