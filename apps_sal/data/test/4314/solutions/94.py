h, w = map(int, input().split())
alist = [''] * h
for i in range(h):
    alist[i] = input()
hlist = []
wlist = []
for i in range(h):
    flag = False
    for j in range(w):
        if alist[i][j] == '
        flag = True
    if flag:
        hlist.append(i)
for i in range(w):
    flag = False
    for j in range(h):
        if alist[j][i] == '
        flag = True
    if flag:
        wlist.append(i)
for i in hlist:
    ans = []
    for j in wlist:
        ans.append(alist[i][j])
    print(''.join(ans))
