N, M, K = list(map(int, input().split()))

friends = [set() for _ in range(N)]
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    friends[a].add(b)
    friends[b].add(a)

blocks = [set() for _ in range(N)]
for _ in range(K):
    c, d = [int(x) - 1 for x in input().split()]
    blocks[c].add(d)
    blocks[d].add(c)

ans = [0] * N
visited = [False] * N
for i in range(N):
    if visited[i]:
        continue
    visited[i] = True
    d = [i]
    check = {i}
    while len(d):
        tmp = d.pop()
        for k in friends[tmp]:
            if visited[k]:
                continue
            d.append(k)
            visited[k] = True
            check.add(k)
    for j in check:
        ans[j] += len(check) - len(friends[j] & check) - len(blocks[j] & check) - 1
print((*ans))
