(N, M, *L) = map(int, open(0).read().split())
dic = [[] for i in range(N + 1)]
rdic = [[] for i in range(N + 1)]
for (a, b, c) in zip(*[iter(L)] * 3):
    dic[a].append(b)
    rdic[b].append(a)
ok1 = [False] * (N + 1)
ok1[1] = True
q = [1]
while q:
    p = q.pop()
    for v in dic[p]:
        if not ok1[v]:
            ok1[v] = True
            q.append(v)
ok2 = [False] * (N + 1)
ok2[N] = True
q = [N]
while q:
    p = q.pop()
    for v in rdic[p]:
        if not ok2[v]:
            ok2[v] = True
            q.append(v)
ok = [a & b for (a, b) in zip(ok1, ok2)]
cnt = 0
dist = [-10 ** 20] * (N + 1)
dist[1] = 0
while True:
    flag = True
    for (a, b, c) in zip(*[iter(L)] * 3):
        if ok[a] & ok[b] and ok[a] != -10 ** 20 and (dist[b] < dist[a] + c):
            flag = False
            dist[b] = dist[a] + c
    if flag:
        print(dist[N])
        break
    cnt += 1
    if cnt > N:
        print('inf')
        break
