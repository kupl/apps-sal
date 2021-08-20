n = int(input())
V = []
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    V.append(a)
    if b < n:
        print('NO')
        quit()
V.sort()
for i in range(n - 1):
    if V[i] <= i:
        print('NO')
        quit()
used = [False] * (n + 1)
tree = []
for i in range(n - 1):
    v = V[i]
    if not used[v]:
        tree.append(v)
        used[v] = True
    else:
        for j in range(1, n + 1):
            if not used[j]:
                tree.append(j)
                used[j] = True
                break
tree.append(n)
print('YES')
for i in range(n - 1):
    print(tree[i], tree[i + 1])
