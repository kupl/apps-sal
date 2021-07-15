n,k=map(int,input().split())
a=list(map(int,input().split()))
s=input()
b=[[s[i],a[i]] for i in range(n)]
ans=0
temp=[]
c=b[0][0]
for i in b:
    if i[0]!=c:
        c=i[0]
        temp.sort(reverse=True)
        ans+=(sum(temp[:min(len(temp),k)]))
        temp.clear()
    if i[0]==c:
        temp.append(i[1])
temp.sort(reverse=True)
ans+=(sum(temp[:min(len(temp),k)]))
print(ans)
