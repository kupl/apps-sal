N, M = map(int, input().split())
bridge = []
size = [1] * (N + 1)
tree = list(range(N + 1))


def find(a):
    x = tree[a]
    if a == x:
        return a
    y = find(x)
    tree[a] = y
    return y


for i in range(M):
    A, B = map(int, input().split())
    bridge.append((A, B))
Ans = N * (N - 1) // 2
ans = []
for a, b in bridge[::-1]:
    aroot = find(a)
    broot = find(b)
    if aroot == broot:
        ans.append(Ans)
        continue
    ans.append(Ans)
    sa = size[aroot]
    sb = size[broot]
    Ans -= sa * sb
    if sa > sb:
        tree[broot] = aroot
        size[aroot] += sb
    else:
        tree[aroot] = broot
        size[broot] += sa
for i in ans[::-1]:
    print(i)
