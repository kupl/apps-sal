N, M = list(map(int, input().split()))
tree = [[] for _ in range(N)]
for _ in range(M):
    u, v = list(map(int, input().split()))
    tree[u - 1].append(v - 1)
S, T = list(map(int, input().split()))
s = S - 1
t = T - 1
ischecked = [[0] * 3 for _ in range(N)]
ischecked[s][0] = 1
ans = -1
q = []
q.append([s, 0])
while q:
    v, c = q.pop(0)
    if v == t and c % 3 == 0:
        ans = c // 3
        break
    for i in tree[v]:
        if ischecked[i][(c + 1) % 3] == 0:
            q.append([i, c + 1])
            ischecked[i][(c + 1) % 3] = 1
print(ans)
