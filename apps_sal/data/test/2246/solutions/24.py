n = int(input())
if n == 1:
    print(0)
    return
graph = [None] * n
for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if graph[u] == None:
        graph[u] = [v]
    else:
        graph[u].append(v)
    if graph[v] == None:
        graph[v] = [u]
    else:
        graph[v].append(u)

is_checked = [False] * n
lens = [None] * n
lens[0] = 0
divs = [None] * n
divs[0] = 1
stack = [0]
ans = 0
while stack:
    top = stack.pop()
    is_checked[top] = True
    vals = graph[top]
    for i in range(len(vals)):
        cur = vals[i]
        if not is_checked[cur]:
            lens[cur] = lens[top] + 1
            divs[cur] = divs[top] * (len(vals) - (1 if top != 0 else 0))
            if len(graph[cur]) == 1:
                ans += lens[cur] / divs[cur]
                is_checked[cur] = None
                lens[cur] = None
                divs[cur] = None
                continue
            stack.append(cur)
print('{:.8f}'.format(ans))
