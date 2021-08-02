import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(200001)
n, m, k = list(map(int, input().split()))
edge = [[]for _ in range(n)]
di = {}
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if a > b: a, b = b, a
    di[(a, b)] = i
    edge[a].append(b)
    edge[b].append(a)
d = [10**10] * n
d[0] = 0
root = [set()for _ in range(n)]
queue = [0]
for node in queue:
    for mode in edge[node]:
        if d[mode] != 10**10:
            if d[mode] + 1 == d[node]:
                root[node].add(mode)
            elif d[mode] == d[node] + 1:
                root[mode].add(node)
            continue
        d[mode] = d[node] + 1
        queue.append(mode)
for i in range(n): root[i] = list(root[i])
t = 1
for i in range(1, n): t *= len(root[i])
print(min(t, k))
for i in range(min(t, k)):
    ans = ["0"] * m
    for j in range(1, n):
        i, jj = divmod(i, len(root[j]))
        ans[di[(min(j, root[j][jj]), max(j, root[j][jj]))]] = "1"
    print("".join(ans))
