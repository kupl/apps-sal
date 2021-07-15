n,c = list(map(int,input().split()))

l = [[] for i in range(c)]
for i in range(n):
    s,t,x = list(map(int,input().split()))
    l[x-1].append([s,t])

al= []
for i in range(c):
    if len(l[i]) > 1:
        l[i].sort()
        now2 = l[i][0][1]
        now1 = l[i][0][0]
        check = False
        for j in range(1,len(l[i])):
            if l[i][j][0] == now2:
                now2 = l[i][j][1]
            else:
                al.append([[now1,now2],i])
                check = True
                now1 = l[i][j][0]
                now2 = l[i][j][1]
        if not check:
            al.append([[now1,now2],i])

    else: 
        if l[i]:
            al.append([l[i][0],i])
al.sort()

count = [[-1,-1]]
for i in range(len(al)):
    a,b,c = al[i][0][0], al[i][0][1],al[i][1]
    check = False
    for j in range(len(count)):
        if count[j][0] < a:
            count[j] = [b,c]
            check = True
            break
    if not check:
        count.append([b,c])

print((len(count)))

