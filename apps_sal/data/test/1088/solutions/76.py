from collections import deque
(n, k) = map(int, input().split())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))


def fact(n):
    tmp = 1
    for i in range(2, n + 1):
        tmp *= i
        tmp %= 998244353
    return tmp


goto = [[] for i in range(n)]
for gyou1 in range(n):
    for gyou2 in range(gyou1 + 1, n):
        OK = True
        for retu in range(n):
            if mat[gyou1][retu] + mat[gyou2][retu] > k:
                OK = False
        if OK:
            goto[gyou1].append(gyou2)
            goto[gyou2].append(gyou1)
que = deque()
gro = [-1] * n
que.append(0)
gro_no = 0
gro[0] = 0
for i in range(n):
    if gro[i] == -1:
        que.append(i)
        gro_no += 1
        gro[i] = gro_no
    while que:
        now = que.popleft()
        for j in goto[now]:
            if gro[j] == -1:
                que.append(j)
                gro[j] = gro_no
gro_cnt = [0] * (gro_no + 1)
for i in range(n):
    gro_cnt[gro[i]] += 1
ans_gyou = 1
for i in range(gro_no + 1):
    ans_gyou *= fact(gro_cnt[i])
goto = [[] for i in range(n)]
for retu1 in range(n):
    for retu2 in range(retu1 + 1, n):
        OK = True
        for gyou in range(n):
            if mat[gyou][retu1] + mat[gyou][retu2] > k:
                OK = False
        if OK:
            goto[retu1].append(retu2)
            goto[retu2].append(retu1)
que = deque()
gro = [-1] * n
que.append(0)
gro_no = 0
gro[0] = 0
for i in range(n):
    if gro[i] == -1:
        que.append(i)
        gro_no += 1
        gro[i] = gro_no
    while que:
        now = que.popleft()
        for j in goto[now]:
            if gro[j] == -1:
                que.append(j)
                gro[j] = gro_no
gro_cnt = [0] * (gro_no + 1)
for i in range(n):
    gro_cnt[gro[i]] += 1
ans_retu = 1
for i in range(gro_no + 1):
    ans_retu *= fact(gro_cnt[i])
ans = ans_gyou * ans_retu % 998244353
print(ans)
