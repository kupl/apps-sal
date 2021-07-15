n,m=list(map(int,input().split()))
l=[]
for i in range(n):
    x=input()
    l.append(x)
ind=list(map(int,input().split()))
ind = list(ind)
se = set(ind)
le = len(l[ind[0]-1])
flag=1
for i in range(m):
    if(len(l[ind[i]-1])!=le):
        flag=0
        break
if flag==1:
    s = ""
    for j in range(le):
        flagc=1
        c=l[ind[0]-1][j]
        for i in range(m):
            if l[ind[i]-1][j]!=c:
                flagc=0
                break
        if flagc==0:
            s=s+"?"
        else:
            s=s+c
    d =[]
    for i in range(n):
        if i+1 not in se:
            if len(l[i])==le:
                d.append(l[i])
    
    for word in d:
        flagw=1
        for i in range(le):
            if s[i]!='?' and s[i]!=word[i]:
                flagw=0
                break
        if flagw==1:
            flag=0
            break
if flag==1:
    print("Yes")
    print(s)
else:
    print("No")
            

