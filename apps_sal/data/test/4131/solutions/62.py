(n, m) = map(int, input().split())
alist = []
for i in range(m):
    (p, y) = map(int, input().split())
    alist.append([i + 1, p, y])
alist.sort(key=lambda x: x[2])
blist = [0] * (n + 1)
ans = [0] * m
for i in range(m):
    blist[alist[i][1]] += 1
    ans1 = '0' * (6 - len(str(alist[i][1])))
    ans2 = str(alist[i][1])
    ans3 = '0' * (6 - len(str(blist[alist[i][1]])))
    ans4 = str(blist[alist[i][1]])
    ans[alist[i][0] - 1] = ans1 + ans2 + ans3 + ans4
for i in range(m):
    print(ans[i])
