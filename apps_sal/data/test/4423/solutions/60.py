N=int(input())
d=[input().split() for i in range(N)]
name=[]
for i in range(N):
    d[i].append(i+1)
    d[i][1]=int(d[i][1])
    name.append(d[i][0])
Name=list(set(name))
Name.sort()
d.sort()
for i in range(len(Name)):
    li=[]
    for j in range(N):
        if Name[i]==d[j][0]:
            li.append([d[j][1],d[j][2]])
        else:
            continue
    li.sort()
    Li=li[::-1]
    for k in range(len(li)):
        print(Li[k][1])
