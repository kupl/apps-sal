(n, m, x) = list(map(int, input().split()))
l = [list(map(int, input().split(' '))) for i in range(n)]
ans = []
for i in range(1 << n):
    cond = [0] * n
    for j in range(n):
        if 1 & i >> j:
            cond[j] = 1
    count = [0] * (m + 1)
    for k in range(n):
        if cond[k] == 1:
            for s in range(m + 1):
                count[s] += l[k][s]
    flag = 0
    for a in range(1, m + 1):
        if count[a] < x:
            flag = 1
            break
    if flag == 0:
        ans.append(count[0])
if ans == []:
    print(-1)
else:
    print(min(ans))
