import itertools
(N, C) = list(map(int, input().split()))
X = []
V = []
for n in range(N):
    (x, v) = list(map(int, input().split()))
    X.append(x)
    V.append(v)
Xr = X[::-1]
Vr = V[::-1]
Xl = [0] + X
Vl = [0] + V
Xr = [0] + [C - x for x in Xr]
Vr = [0] + Vr
Vl = list(itertools.accumulate(Vl))
Vr = list(itertools.accumulate(Vr))


def update_mx(ls):
    mx = 0
    for i in range(len(ls)):
        mx = max(mx, ls[i])
        ls[i] = mx
    return ls


def create(V, X, k):
    ls = []
    for n in range(N + 1):
        ls.append(V[n] - k * X[n])
    return update_mx(ls)


L = create(Vl, Xl, 1)
Lt = create(Vl, Xl, 2)
R = create(Vr, Xr, 1)
Rt = create(Vr, Xr, 2)
ans = 0
for n in range(N + 1):
    ans = max(ans, Lt[n] + R[N - n])
    ans = max(ans, Rt[n] + L[N - n])
print(ans)
