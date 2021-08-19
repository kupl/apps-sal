(n, m) = [int(x) for x in input().split()]
visited = [[True for i in range(m + 2)]]
visited += [[True] + [False if c == '.' else True for c in input()] + [True] for i in range(n)]
visited += [[True for i in range(m + 2)]]
start = tuple((int(x) for x in input().split()))
finish = tuple((int(x) for x in input().split()))
visited[start[0]][start[1]] = False


def neighbours(p):
    return ((p[0] + 1, p[1]), (p[0], p[1] + 1), (p[0] - 1, p[1]), (p[0], p[1] - 1))


gates = [p for p in neighbours(finish) if not visited[p[0]][p[1]]]


def DFS(p, gates):
    stack = [p]
    while stack:
        node = stack.pop()
        if node in gates:
            return True
        (x, y) = node
        if visited[x][y]:
            continue
        visited[x][y] = True
        stack.extend(neighbours(node))
    return False


if finish == start and len(gates) > 0:
    print('YES')
elif not visited[finish[0]][finish[1]] and len(gates) < 2 or len(gates) == 0:
    print('NO')
else:
    print('YES' if DFS(start, gates) else 'NO')
