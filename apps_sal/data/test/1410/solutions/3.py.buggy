from itertools import permutations


def cost(start, C):
    prev = start
    color = 0
    mycost = C[color][start]
    color = (color + 1) % 3
    cur = tree[start][0]
    for _ in range(n - 1):
        #print(prev, cur, tree[cur])
        glnext[prev] = cur
        mycost += C[color][cur]
        if prev != tree[cur][0]:
            prev = cur
            cur = tree[cur][0]
        elif len(tree[cur]) > 1:
            prev = cur
            cur = tree[cur][1]
        color = (color + 1) % 3
    return mycost


n = int(input())
c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))
C = [c1, c2, c3]
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    tree[u].append(v)
    tree[v].append(u)
for node in tree:
    if len(node) > 2:
        print(-1)
        return
for i in range(n):
    if len(tree[i]) == 1:
        start = i
        break
best = 999999999999999999
glnext = [-1] * n
for p in permutations(list(range(3))):
    Cperm = [C[p[0]], C[p[1]], C[p[2]]]
    cst = cost(start, Cperm)
    if cst < best:
        best = cst
        ans = [-1] * n
        cur = start
        col = 0
        for _ in range(n):
            ans[cur] = p[col] + 1
            cur = glnext[cur]
            col = (col + 1) % 3
print(best)
print(' '.join(list(map(str, ans))))
