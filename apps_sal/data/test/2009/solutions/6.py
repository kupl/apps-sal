def add(ans, r, c):
    if cells[r][c] == '0':
        cells[r][c] = '1'
        rc = r, c
        ans.append(rc)


def dfs(r, c):
    ans = [(r, c)]
    for r, c in ans:
        if c != 1:
            add(ans, r, c - 1)
        if c != n:
            add(ans, r, c + 1)
        if r != 1:
            add(ans, r - 1, c)
        if r != n:
            add(ans, r + 1, c)
    return ans


n = int(input())
r1, c1 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))
res = 5000
cells = (['1'],) + tuple((['1'] + list(input()) for _ in range(n)))
dfs1 = dfs(r1, c1)
for rs, cs in dfs(r2, c2):
    for rt, ct in dfs1:
        res = min(res, (rs - rt) ** 2 + (cs - ct) ** 2)
print(res)
