n=input()
b=[]
b=n.split()
n=int(b[0])
k=int(b[1])
q=int(b[2])
c=input()
level=c.split()
online=[]
for i in range(q):
    c=input()
    z=c.split()
    if z[0]=='1':
        if len(online)<k:
            online.append(int(z[1]))
        else:
            min=int(level[int(z[1])-1])
            number=-1
            for j in range(k):
                if int(level[online[j]-1])<min:
                    min=int(level[online[j]-1])
                    number=j
            if number>-1:
                online[number]=int(z[1])
    else:
        if online.count(int(z[1]))>0:
            print('YES')
        else:
            print('NO')


