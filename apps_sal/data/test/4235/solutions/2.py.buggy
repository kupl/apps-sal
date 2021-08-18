import sys


def input():
    return sys.stdin.readline()


n, m = map(int, input().split())
give = [False] * (n + 1)
take = [False] * (n + 1)
edge = dict()
inputs = []
for i in range(n):
    edge[i + 1] = []
for i in range(m):
    u, v = map(int, input().split())
    inputs.append((u, v))
    edge[u].append(v)
    edge[v].append(u)
check = [False] * (n + 1)
queue = [1]
front = 0
while front < len(queue):
    u = queue[front]
    check[u] = True
    for v in edge[u]:
        if check[v]:
            continue
        queue.append(v)
        if (give[u] and give[v]) or (take[u] and take[v]):
            print('NO')
            return
        if (give[u] and take[v]) or (take[u] and give[v]):
            continue
        if give[u]:
            take[v] = True
            continue
        if take[u]:
            give[v] = True
            continue
        if give[v]:
            take[u] = True
            continue
        if take[v]:
            give[u] = True
            continue
        give[u] = True
        take[v] = True
    front += 1
print('YES')
for u, v in inputs:
    if give[u] and take[v]:
        print(1, end="")
    else:
        print(0, end="")
print()
