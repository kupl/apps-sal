# BFSだとかえって考えにくい
# それぞれの頂点に対して塗られてない色で塗り分け
n = int(input())
paths = [[] for i in range(n)]
colors = [0] * (n - 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    paths[a - 1].append(i)
    paths[b - 1].append(i)
m = 0
for i in range(n):
    m = max(m, len(paths[i]))
print(m)
# print(paths)
for i in range(n):
    cand1, cand2 = set(), []
    # print(paths[i])
    for j in paths[i]:
        if colors[j] != 0:
            cand1.add(colors[j])
        else:
            cand2.append(j)
    now = 1
    for j in cand2:
        while now in cand1:
            now += 1
        colors[j] = now
        now += 1
for i in range(n - 1):
    print(colors[i])
