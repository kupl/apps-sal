n = int(input())
d = []
v = []
for i in range(n):
    (a, b) = map(int, input().split())
    v.append([a, b, i])
g = dict()
for i in range(n + 20):
    g[i] = set()
for i in v:
    if i[0] in g:
        g[i[0]].add(i[2])
    else:
        g[i[0]] = set()
        g[i[0]].add(i[2])
ans = []
while len(g[1]) > 0:
    i = g[1].pop()
    a = v[i][2]
    b = v[i][1]
    g[v[a][0]].discard(v[a][2])
    g[v[a][0] - 1].add(v[a][2])
    v[a][0] -= 1
    g[v[b][0]].discard(v[b][2])
    g[v[b][0] - 1].add(v[b][2])
    v[b][0] -= 1
    v[b][1] ^= a
    ans.append((a, b))
print(len(ans))
for i in ans:
    print(*i)
'\n9\n2 5\n4 3\n7 6\n8 3\n5 0\n6 1\n3 9\n1 0\n9 0\n'
