import sys
input = sys.stdin.readline


n = int(input())
info = [list(map(int, input().split())) for i in range(n - 1)]

tree = [[] for i in range(n)]
memo = {}
for i in range(n - 1):
    a, b = info[i]
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    tree[a].append(b)
    tree[b].append(a)
    memo[a * 1000000 + b] = i
ans = [-1] * (n - 1)
pos = 0
for i in range(n):
    if len(tree[i]) == 1:
        a, b = i, tree[i][0]
        if a > b:
            a, b = b, a
        ans[memo[a * 1000000 + b]] = pos
        pos += 1
for i in range(n - 1):
    if ans[i] == -1:
        ans[i] = pos
        pos += 1
if n == 2:
    print(0)
    return
for i in ans:
    print(i)
