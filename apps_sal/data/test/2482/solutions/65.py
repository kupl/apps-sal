import collections
N, K, L = map(int, input().split())

par = [i for i in range(N)]


def find(x, P):
    if P[x] == x:
        return x
    else:
        b = find(P[x], P)
        P[x] = b
        return b


def unite(x, y, P):
    root_x = find(x, P)
    root_y = find(y, P)
    if root_y > root_x:
        P[root_x] = root_y
    else:
        P[root_y] = root_x


par2 = [i for i in range(N)]

for _ in range(K):
    p, q = map(int, input().split())
    unite(p - 1, q - 1, par)

for _ in range(L):
    p, q = map(int, input().split())
    unite(p - 1, q - 1, par2)
# print(par2)

r = []
for i in range(N):
    r.append((find(i, par), find(i, par2)))

count = collections.Counter(r)
# print(count)

for i in range(N):
    ans = count[r[i]]
    if i == N - 1:
        print(ans)
    else:
        print(ans, end=' ')
