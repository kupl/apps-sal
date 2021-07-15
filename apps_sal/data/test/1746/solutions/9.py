n = int(input())
leaf = [True]*(n+1)
chd = [-1]*(n+1)
for i in range(2,n+1):
    p = int(input())
    if chd[p] == -1:
        chd[p] = [i]
        leaf[p] = False
    else:
        chd[p].append(i)
suc = True
for i in range(1,n+1):
    ctr = 0
    if not leaf[i]:
        for x in chd[i]:
            if leaf[x]:
                ctr += 1
        if ctr < 3:
            suc = False
            break

if suc:
    print('Yes')
else:
    print('No')

