(n, m) = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    (a, b) = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
print('\n'.join(list(map(lambda x: str(len(x)), edge))))
