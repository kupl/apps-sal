import itertools
n = int(input())
for _ in range(n):
    s = list(input())
    t = list(input())
    sgr = itertools.groupby(s)
    tgr = itertools.groupby(t)
    slist = []
    tlist = []
    for key, group in sgr:
        slist.append([key, len(list(group))])
    for key, group in tgr:
        tlist.append([key, len(list(group))])
    if len(slist) != len(tlist):
        print("NO")
    else:
        flag = 1
        for i in range(len(slist)):
            if slist[i][0] == tlist[i][0] and slist[i][1] <= tlist[i][1]:
                continue
            else:
                flag = 0
                break
        if flag == 1:
            print("YES")
        else:
            print("NO")

