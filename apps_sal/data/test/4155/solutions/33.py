n=int(input())
a=list(map(int,input().split()))

r=0
b=[a]
while True:
    d=[]
    for x in b:
        m=min(x)
        r+=m
        d.append([i-m for i in x])

    b=[]
    for x in d:
        t=[]
        for y in range(len(x)):
            if y==len(x)-1:
                if x[y]!=0:
                    t.append(x[y])
                    b.append(t)
                if x[y]==0 and x[y-1]!=0:b.append(t)
            elif x[y]!=0:t.append(x[y])
            elif x[y]==0:
                if len(t)!=0:b.append(t)
                t=[]

    d=[]
    for x in b:
        if len(x)<=2:r+=max(x)
        else:d.append(x)
    if len(d)==0:print(r);return
    b=d
