from typing import List, Tuple


def solve(n: int, m: int, k: int, chart: List[List[str]]):

    visited = [[0] * m for _ in range(n)]

    def dfs(x: int, y: int) -> List[Tuple[int, int]]:
        stack = [(x, y)]
        component = set([(x, y)])
        is_ocean = False
        while stack:
            a, b = stack.pop()
            visited[a][b] = 1
            if a == 0 or a == n - 1 or b == 0 or b == m - 1:
                is_ocean = True
            for ao, bo in [(a, b + 1), (a, b - 1), (a + 1, b), (a - 1, b)]:
                if 0 <= ao < n and 0 <= bo < m:
                    if not visited[ao][bo] and chart[ao][bo] == '.':
                        stack.append((ao, bo))
                        component.add((ao, bo))
        if not is_ocean:
            return list(component)

    lakes = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if not visited[i][j] and chart[i][j] == '.':
                lake = dfs(i, j)
                if lake:
                    lakes.append(lake)
    changes = 0
    for component in sorted(lakes, key=len)[:len(lakes) - k]:
        for x, y in component:
            changes += 1
            chart[x][y] = '*'
    return changes, chart


n, m, k = list(map(int, input().split()))
chart = [list(input()) for _ in range(n)]
changes, new_chart = solve(n, m, k, chart)
print(changes)
for line in new_chart:
    print(''.join(line))
