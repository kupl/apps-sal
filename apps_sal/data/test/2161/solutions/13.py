n=int(input())
s=set()
arr=[]
a={}
for i in range(n):
    rr=list(map(str,input().strip().split(' ')))
    arr.append(rr)
for i in range(n):
    t=arr[i]
    s.add(t[0])
    try:
        p=a[t[0]]
        for j in range(2,2+int(t[1])):
            a[t[0]].append(t[j])
    except:
        p=t[2]
        a[t[0]]=[p]
        for j in range(3,2+int(t[1])):
            a[t[0]].append(t[j])

for ii in s:
    p=a[ii]
    p=list(set(p))
    
    for i in range(len(p)):
        if(p[i]!='-1'):
            tt=p[i]
            for j in range(len(p)):
                if(j!=i):
                    pp=p[j]
                    if(len(pp)>=len(tt)):
                        continue
                    else:
                        y=0
                        ans=0
                        for uu in range(len(tt)-len(pp),len(tt)):
                            if(tt[uu]!=pp[y]):
                                ans=1
                            y+=1
                        if(ans==0):
                            p[j]='-1'
    d=[]
    
    cnt=0
    for oo in p:
        if(oo!='-1'):
            cnt+=1
    d.append(cnt)

    for oo in p:
        if(oo!='-1'):
            d.append(oo)

    a[ii]=d
print(len(s))
for i in s:
    print(i,end=' ')
    t=a[i]
    for j in t:
        print(j,end=' ')
    print()


