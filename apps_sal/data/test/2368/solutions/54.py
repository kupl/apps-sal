import collections
N, M = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = [list(map(int, input().split())) for l in range(M)]

par = [i for i in range(N)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y


for i in l:
    unite(i[0] - 1, i[1] - 1)

for i in range(N):
    find(i)


c = collections.Counter(par)
sumcheck = [[0] * N, [0] * N]

for i in range(N):
    sumcheck[0][par[i]] += a[i]
    sumcheck[1][par[i]] += b[i]

if sumcheck[0] == sumcheck[1]:
    print("Yes")
else:
    print("No")
