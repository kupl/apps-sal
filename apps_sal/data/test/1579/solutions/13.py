import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n = int(readline())
xy = list(map(int, read().split()))
XY = list(zip(xy, xy))
max_num = 10 ** 5
delta = 10 ** 5 + 10
graph = [[] for _ in range(max_num + delta + 1)]
for (x, y) in XY:
    graph[x].append(delta + y)
    graph[delta + y].append(x)
x_used = [False] * (max_num + 1)
y_used = [False] * (max_num + 1)


def dfs(idx):
    x_res = 0
    y_res = 0
    edgenum = 0
    stack = []
    stack.append(idx)
    if idx >= delta:
        y_used[idx % delta] = True
    else:
        x_used[idx] = True
    while stack:
        v = stack.pop()
        if v >= delta:
            y_res += 1
        else:
            x_res += 1
        for u in graph[v]:
            if u >= delta:
                if y_used[u % delta]:
                    continue
                y_used[u % delta] = True
            else:
                if x_used[u]:
                    continue
                x_used[u] = True
            edgenum += 1
            stack.append(u)
    res = x_res * y_res
    return res


ans = 0
for i in range(max_num + 1):
    if x_used[i]:
        continue
    temp = dfs(i)
    ans += temp
for i in range(max_num + 1):
    if y_used[i]:
        continue
    i += delta
    temp = dfs(i)
    ans += temp
print(ans - n)
