n=int(input())
a=list(map(int,input().split()))
dic={}
for i in range(n):
    sm=0
    for j in range(i,n):
        sm+=a[j]
        if sm in dic:
            dic[sm].append((i,j))
        else:
            dic[sm]=[(i,j)]
ans=0
anskey=-1
for key in dic:
    cnt=0
    last=-1
    for a,b in sorted(dic[key]):
        if a>last:
            cnt+=1
            last=b
        elif b<last:
            last=b
    if cnt>ans:
        ans=cnt
        anskey=key
last=-1
tmp=[]
for a,b in sorted(dic[anskey]):
    if a>last:
        last=b
        tmp.append(str(a+1)+" "+str(b+1))
    elif b<last:
        last=b
        tmp.pop()
        tmp.append(str(a+1)+" "+str(b+1))
print(ans,'\n'.join(tmp),sep='\n')
