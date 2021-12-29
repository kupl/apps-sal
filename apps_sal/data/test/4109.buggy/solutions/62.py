import itertools
(N, M, X) = map(int, input().split())
lsC = []
lsM = []
for i in range(N):
    ls = list(map(int, input().split()))
    C = ls.pop(0)
    lsC.append(C)
    lsM.append(ls)
lsP = itertools.product(range(2), repeat=N)
ans = 10 ** 15
for i in lsP:
    Call = 0
    lsAll = [0] * M
    f = True
    for j in range(N):
        if i[j] == 1:
            Call += lsC[j]
            for k in range(M):
                lsAll[k] += lsM[j][k]
    for l in range(M):
        if lsAll[l] < X:
            f = False
            break
    if f:
        ans = min(ans, Call)
if ans == 10 ** 15:
    print(-1)
else:
    print(ans)
