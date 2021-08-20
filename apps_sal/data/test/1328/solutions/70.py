import copy
(N, Ma, Mb) = map(int, input().split())
a = [0 for k in range(N)]
b = [0 for k in range(N)]
c = [0 for k in range(N)]
for k in range(N):
    (a[k], b[k], c[k]) = map(int, input().split())
Sa = sum(a)
Sb = sum(b)
dp = [[[5000 for k in range(Sb + 1)] for k in range(Sa + 1)] for k in range(N + 1)]
dp[0][0][0] = 0
for k in range(N):
    listj = []
    listl = []
    for j in range(Sa - a[k] + 1):
        for l in range(Sb - b[k] + 1):
            if dp[k][j][l] != 5000:
                listj.append(j)
                listl.append(l)
    for m in range(len(listl)):
        dp[k + 1][listj[m] + a[k]][listl[m] + b[k]] = min(dp[k][listj[m]][listl[m]] + c[k], dp[k][listj[m] + a[k]][listl[m] + b[k]])
        dp[k + 1][listj[m]][listl[m]] = min(dp[k][listj[m]][listl[m]], dp[k + 1][listj[m]][listl[m]])
ans = [5000]
for k in range(1, min(Sa // Ma, Sb // Mb) + 1):
    ans.append(dp[-1][Ma * k][Mb * k])
if min(ans) == 5000:
    print(-1)
else:
    print(min(ans))
