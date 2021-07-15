from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

n = int(input())
r1, c1 = [int(i) for i in input().split()]
r2, c2 = [int(i) for i in input().split()]
MAP = [[int(s) for s in input()] for i in range(n)]
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

def dfs(r, c, mark, A):
    if r < 0 or r >= n or c < 0 or c >= n:
        return
    if MAP[r][c] == 1:
        return
    if MAP[r][c] == mark:
        return
    A.append((r, c))
    MAP[r][c] = mark
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        dfs(r+dr, c+dc, mark, A)

A = []
dfs(r1, c1, 2, A)
if MAP[r1][c1] == MAP[r2][c2]:
    print(0)
    return
B = []
dfs(r2, c2, 3, B)

ans = 2 * n ** 2
for a, b in A:
    ans = min(ans, min((a - c) ** 2 + (b - d) ** 2 for c, d in B))

print(ans)
