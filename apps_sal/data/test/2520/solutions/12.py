import sys
(N, M, K) = map(int, input().split())
friends = [set() for _ in range(N)]
for _ in range(M):
    (a, b) = map(int, sys.stdin.readline().split())
    friends[a - 1].add(b - 1)
    friends[b - 1].add(a - 1)
blocks = [set() for _ in range(N)]
for _ in range(K):
    (c, d) = map(int, sys.stdin.readline().split())
    blocks[c - 1].add(d - 1)
    blocks[d - 1].add(c - 1)
done = set()
chains = []
todo = []
for s in range(N):
    if s in done:
        continue
    chain = set()
    todo.append(s)
    while todo:
        i = todo.pop()
        for ni in friends[i]:
            if ni in done:
                continue
            done.add(ni)
            chain.add(ni)
            todo.append(ni)
    chains.append(chain)
ans = [0] * N
for chain in chains:
    for i in chain:
        blocks[i].intersection_update(chain)
        ans[i] = len(chain) - len(blocks[i]) - len(friends[i]) - 1
print(' '.join(map(str, ans)))
