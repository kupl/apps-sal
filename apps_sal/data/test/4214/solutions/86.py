n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]


def distance(i, j):
    xi, yi = xy[i]
    xj, yj = xy[j]
    return (xi - xj)**2 + (yi - yj)**2


visited = [False] * n
ans = 0


def dfs(route, length):
    nonlocal ans
    if len(route) == n:
        ans += length
        return
    else:
        for i in range(n):
            if visited[i]:
                continue
            next_distance = distance(route[-1], i)**0.5
            visited[i] = True
            dfs(route + [i], length + next_distance)
            visited[i] = False


cnt = 1
for i in range(n):
    cnt *= i + 1
    visited[i] = True
    dfs([i], 0)
    visited[i] = False
print((ans / cnt))
