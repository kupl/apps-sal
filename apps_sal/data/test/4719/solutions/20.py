n=int(input())
abc='abcdefghijklmnopqrstuvwxyz'
s=[]
t=[51]*len(abc)
#print(t)
for i in range(n):
    u=input()
    for j in range(len(abc)):
        v=u.count(abc[j])
        t[j]=min(t[j],v)
ans=''
for j in range(len(abc)):
    ans+=t[j]*abc[j]
print(ans)
