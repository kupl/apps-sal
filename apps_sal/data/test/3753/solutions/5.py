import sys
n, m = list(map(int, input().split()))

# fields = ['#' * (2 + m)] + ['#' + input() + '#' for i in range(n)] + ['#' * (2 + m)]
fields = ['#' * (2 + m)] + ['#' + sys.stdin.readline().rstrip() + '#' for i in range(n)] + ['#' * (2 + m)]

visited = [[False] * (m + 2) for i in range(n + 2)]

for i in range(2):
    q = [(1, 1)]

    while q:
        x, y = q.pop()

        if visited[x][y]:
            continue

        visited[x][y] = True

        if fields[x+1][y] != '#' and not visited[x+1][y]:
            q.append((x+1, y))
        if fields[x][y+1] != '#' and not visited[x][y+1]:
            q.append((x, y+1))

        if x == n and y == m:
            break

    if x != n or y != m:
        print(i)
        return

    visited[1][1] = False
    visited[n][m] = False

print(2)







