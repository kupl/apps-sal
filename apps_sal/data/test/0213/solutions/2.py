(n, m) = map(int, input().split())
a = []
for i in range(m):
    (k, f) = map(int, input().split())
    a.append((k, f))
fl = []
ps = 0
val = -1
for i in range(1, 1000):
    flag = 1
    for j in range(m):
        if (a[j][0] - 1) // i != a[j][1] - 1:
            flag = 0
    if flag:
        ps += 1
        fl.append(i)
ans = []
for i in range(len(fl)):
    ans.append((n - 1) // fl[i] + 1)
if not len(ans):
    print(-1)
else:
    tmp = ans[0]
    flag = 1
    for i in range(len(ans)):
        if ans[i] != tmp:
            flag = 0
    if not flag:
        print(-1)
    else:
        print(ans[0])
