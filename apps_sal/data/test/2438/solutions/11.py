from sys import stdin,stdout
n=int(stdin.readline().strip())
s=stdin.readline().strip()
acumA=[0 for i in range(n+3)]
acumB=[0 for i in range(n+3)]
dictA=[-1 for i in range(n+3)]
dictB=[-1 for i in range(n+3)]
for i in range(n):
    if i!=0:
        acumA[i]+=acumA[i-1]
        acumB[i]+=acumB[i-1]
    if s[i]=="A":
        acumA[i]+=1
        dictA[acumA[i]]=i
    
    if s[i]=="B":
        acumB[i]+=1
        dictB[acumB[i]]=i
ans=0
for i in range(n-1):
    if s[i]=="A":
        if(dictA[acumA[i]+1]==-1):
            continue
        x=dictB[acumB[i]+1]
        if(x==-1):
            x=n
        ans+=(x-i-1)
        x=dictB[acumB[i]+1]
        if(x==-1):
            continue
        x=max(dictB[acumB[i]+1],dictA[acumA[i]+1]-1)

        ans+=(n-x-1)
    else:
        if(dictB[acumB[i]+1]==-1):
            continue
        x=dictA[acumA[i]+1]
        if(x==-1):
            x=n
        ans+=(x-i-1)
        x=dictA[acumA[i]+1]
        if(x==-1):
            continue
        x=max(dictA[acumA[i]+1],dictB[acumB[i]+1]-1)
        ans+=(n-x-1)
print(ans)

