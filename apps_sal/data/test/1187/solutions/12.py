def iscyclic(s, visited, restack):
    visited[s] = True
    restack[s] = True

    if s in adj:
        for u in adj[s]:
            if visited[u] == False:
                if iscyclic(u, visited, restack) == True:
                    return True
            elif restack[u] == True:
                return True
    restack[s] = False
    return False


def cyclic():
    visited = [False] * (n + 1)
    restack = [False] * (n + 1)
    for u in adj:
        if visited[u] == False:
            if iscyclic(u, visited, restack) == True:
                return True
    return False


n, m = map(int, input().split())
adj = {}
l = []
for i in range(m):
    a, b = map(int, input().split())
    if a not in adj:
        adj[a] = [b]
    else:
        adj[a].append(b)
    l.append([a, b])
visited = [False] * (n + 1)
bo = cyclic()
if bo == False:
    print(1)
    for i in range(m):
        print(1, end=" ")
else:
    print(2)
    for i in range(m):
        if l[i][0] > l[i][1]:
            print(2, end=" ")
        else:
            print(1, end=" ")
