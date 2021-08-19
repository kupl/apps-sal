from sys import stdin
input = stdin.readline


def put():
    return map(int, input().split())


def dfs():
    s = [(0, 0)]
    tree[0].append(1)
    while s:
        (i, p) = s.pop()
        c = 1
        for j in tree[i]:
            if j != p:
                s.append((j, i))
                while c in [color[i], color[p]]:
                    c += 1
                color[j] = c
                c += 1


n = int(input())
tree = [[] for i in range(n + 1)]
color = [0] * (n + 1)
for _ in range(n - 1):
    (x, y) = put()
    tree[x].append(y)
    tree[y].append(x)
ans = 0
for i in range(1, n + 1):
    ans = max(ans, len(tree[i]) + 1)
dfs()
print(ans)
print(*color[1:])
