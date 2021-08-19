import statistics
(N, M) = map(int, input().split())
A = [0] * M
B = [0] * M
par = [-1] * N


def find(x):
    if par[x] < 0:
        return x
    else:
        tank = []
        while par[x] >= 0:
            tank.append(x)
            x = par[x]
        for elt in tank:
            par[elt] = x
        return x


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        par[x] += par[y]
        par[y] = x
        return True


for i in range(M):
    (A[i], B[i]) = sorted(map(int, input().split()))
    unite(A[i] - 1, B[i] - 1)
for i in range(N):
    par[i] *= -1
print(max(par))
