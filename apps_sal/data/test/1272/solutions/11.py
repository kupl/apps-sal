def root(i):
    if par[i] < 0:
        return i
    else:
        return root(par[i])


def size(a):
    return -par[root(a)]


def union(a, b):
    a = root(a)
    b = root(b)
    if a == b:
        return False
    if size(a) < size(b):
        a, b = b, a
    par[a] += par[b]
    par[b] = a
    return True


n, m = map(int, input().split())
bridge = []
for i in range(m):
    bridge.append([int(j) - 1 for j in input().split()])
ans = [n * (n - 1) // 2]
par = [-1 for _ in range(n)]

for a, b in bridge[::-1]:
    if root(a) == root(b):
        ans.append(ans[-1])
    else:
        ans.append(ans[-1] - size(a) * size(b))
        union(a, b)
ans = ans[::-1]
for i in ans[1:]:
    print(i)
