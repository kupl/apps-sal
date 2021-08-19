(N, M) = map(int, input().split())
tree = [[] for _ in range(N)]
for i in range(M):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)
for i in range(N):
    print(len(tree[i]))
