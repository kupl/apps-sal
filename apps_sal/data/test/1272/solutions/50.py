import sys
sys.setrecursionlimit(10 ** 6)
(N, M) = map(int, input().split())
bridge = []
size = [1] * (N + 1)
tree = list(range(N + 1))


def find(a):
    x = tree[a]
    if a == x:
        return a
    x = find(x)
    tree[a] = x
    return x


for i in range(M):
    (A, B) = map(int, input().split())
    bridge.append((A, B))
Ans = N * (N - 1) // 2
ans = []
for (a, b) in bridge[::-1]:
    aroot = find(a)
    broot = find(b)
    if aroot == broot:
        ans.append(Ans)
        continue
    ans.append(Ans)
    Ans -= size[aroot] * size[broot]
    tree[broot] = aroot
    size[aroot] += size[broot]
for i in ans[::-1]:
    print(i)
