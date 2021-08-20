import sys
input = sys.stdin.readline


def dfs():
    stack = [(0, 0)]
    d[0].append(1)
    while stack:
        (i, p) = stack.pop()
        c = 1
        for j in d[i]:
            if j != p:
                stack.append((j, i))
                while c in {color[i], color[p]}:
                    c = c + 1
                color[j] = c
                c = c + 1


n = int(input())
d = {}
d[0] = []
for _ in range(n - 1):
    (x, y) = map(int, input().split())
    if x in d:
        d[x].append(y)
    else:
        d[x] = [y]
    if y in d:
        d[y].append(x)
    else:
        d[y] = [x]
m = 0
for i in d:
    if len(d[i]) > m:
        m = len(d[i])
ans = m + 1
color = [-1] * (n + 1)
dfs()
print(ans)
print(*color[1:])
