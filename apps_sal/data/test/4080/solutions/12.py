(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
Lf = [[] for _ in range(n)]
Rb = [[] for _ in range(n)]
LR = []
for i in range(m):
    (l, r) = list(map(int, input().split()))
    (l, r) = (l - 1, r - 1)
    Lf[r].append(l)
    Rb[l].append(r)
    LR.append((l, r))
minus = [0] * n
INF = 10 ** 18
ans = [-INF] * n
mn = A[0]
for i in range(n):
    ans[i] = max(ans[i], A[i] - mn)
    for l in Lf[i]:
        for j in range(l, i + 1):
            minus[j] -= 1
            mn = min(mn, A[j] + minus[j])
    mn = min(mn, A[i] + minus[i])
minus = [0] * n
mn = A[n - 1]
for i in reversed(list(range(n))):
    ans[i] = max(ans[i], A[i] - mn)
    for r in Rb[i]:
        for j in range(i, r + 1):
            minus[j] -= 1
            mn = min(mn, A[j] + minus[j])
    mn = min(mn, A[i] + minus[i])
ans_ = max(ans)
res = []
for i in range(n):
    if ans[i] == ans_:
        for j in range(m):
            (l, r) = LR[j]
            if not (l <= i and i <= r):
                res.append(j + 1)
        break
print(ans_)
print(len(res))
print(*res)
