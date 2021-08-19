import itertools
(n, m) = map(int, input().split())
edge = [[] for i in range(n + 1)]
for i in range(m):
    (a, b) = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
ans = 0
for junretu in list(itertools.permutations(list(range(2, n + 1)))):
    now = 1
    flag = True
    for i in list(junretu):
        if not i in edge[now]:
            flag = False
            break
        now = i
    if flag:
        ans += 1
print(ans)
