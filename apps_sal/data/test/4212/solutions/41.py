n, m, q = map(int, input().split())
abcd = []
for i in range(q):
    a, b, c, d = map(int, input().split())
    abcd.append([a, b, c, d])


def dfs(i, j):
    if i == 0:
        alist = []
        for k in range(j):
            alist.append([k + 1])
        return alist
    elif i > 0 and i <= n:
        blist = []
        for k in dfs(i - 1, j):
            last = k[-1]
            for l in range(last, j + 1):
                clist = k.copy()
                clist.append(l)
                blist.append(clist)
        return blist


ans = 0
for alist in dfs(n - 1, m):
    cnt = 0
    for i in range(q):
        if alist[abcd[i][1] - 1] - alist[abcd[i][0] - 1] == abcd[i][2]:
            cnt += abcd[i][3]
    ans = max(ans, cnt)
print(ans)
