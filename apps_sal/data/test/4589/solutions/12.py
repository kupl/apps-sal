from itertools import product as pro
h, w = list(map(int, input().split()))
s = [list(input()) for i in range(h)]
ans = [["
visited = []


def dfs(p):
    if p in visited or s[p[0]][p[1]] == "
        return None

    temp = [1 if s[y + p[0]][x + p[1]] == '
    s[p[0]][p[1]] = sum(temp)


for i in range(len(s)):
    for j in range(len(s[0])):
        dfs([i, j])


for i in s:
    print((''.join(map(str, i))))
