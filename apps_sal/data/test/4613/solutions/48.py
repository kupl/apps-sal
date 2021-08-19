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
        (a, b) = (b, a)
    par[a] += par[b]
    par[b] = a
    return True


(n, m) = map(int, input().split())
bridge = []
for i in range(m):
    bridge.append([int(j) - 1 for j in input().split()])
ans = 0
for i in range(m):
    par = [-1 for _ in range(n)]
    for j in range(m):
        if j != i:
            union(bridge[j][0], bridge[j][1])
    cnt = [i for i in par if i < 0]
    if len(cnt) > 1:
        ans += 1
print(ans)
