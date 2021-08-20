import copy
(N, M) = map(int, input().split())
l = []
for i in range(M):
    l.append(list(map(int, input().split())))


def bfs(l, tmp, came):
    t = []
    for n in tmp:
        for s in l:
            if s[0] == n and s[1] not in came:
                t.append(s[1])
                came.append(s[1])
            elif s[1] == n and s[0] not in came:
                t.append(s[0])
                came.append(s[0])
    if t == []:
        came = set(came)
        return came
    else:
        return bfs(l, t, came)


ans = 0
for i in range(M):
    x = copy.copy(l)
    x.pop(i)
    a = bfs(x, [1], [1])
    if len(a) < N:
        ans += 1
print(ans)
