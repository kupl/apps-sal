import sys

read = sys.stdin.read

N, M = list(map(int, input().split()))
if M != 0:
    AB = list(map(int, read().split()))
else:
    print((-1))
    return

graph = [[] for _ in range(N + 1)]
A = AB[::2]
B = AB[1::2]
A_s = set(A)
# 出次数が0の頂点はいらない。
needless = set(range(1, N + 1)) - A_s

for i, j in zip(A, B):
    if j not in needless:
        graph[i].append(j)


# cycleを少なくとも一つ検出する
def dfs(original_stack):
    checked = [False] * (N + 1)
    while original_stack:
        start = original_stack.pop()
        if checked[start]:
            continue
        checked[start] = True
        stack = [(start, [start])]
        while stack:
            v, route = stack.pop()
            for i in graph[v]:
                if i in route:
                    return route[route.index(i):]
                else:
                    stack.append((i, route + [i]))
                    checked[i] = True


v = dfs([i for i in range(1, N + 1) if graph[i]])
if not v:
    print((-1))
    return

while True:
    v_s = set(v)
    length = len(v)
    for i, (v_i, v_j) in enumerate(zip(v, v[1:] + [v[0]])):
        for j in graph[v_i]:
            if j != v_j and j in v_s:
                idx = v.index(j)
                if i < idx:
                    v = v[:i + 1] + v[idx:]
                else:
                    v = v[idx:i + 1]
                break
        else:
            continue
        break
    else:
        print((len(v)))
        print(('\n'.join(map(str, v))))
        return

