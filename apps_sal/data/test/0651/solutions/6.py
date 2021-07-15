from itertools import permutations
n, m = list(map(int, input().split()))
M = [input() for i in range(n)]
for i in range(n):
    for j in range(m):
        if M[i][j] == 'S':
            sx = j; sy = i
        elif M[i][j] == 'E':
            ex = j; ey = i
*S, = list(map(int, input()))

dd = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def solve(p):
    x = sx; y = sy
    for c in S:
        dx, dy = dd[p[c]]
        x += dx; y += dy
        if (not 0 <= x < m) or (not 0 <= y < n) or (M[y][x] == '#'):
            return 0
        if x == ex and y == ey:
            return 1
    return 0

ans = 0
for p in permutations(list(range(4))):
    ans += solve(p)
print(ans)

