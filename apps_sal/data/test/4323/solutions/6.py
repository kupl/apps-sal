n,money=map(int,input().split())
ans=[]
for _ in range(n):
    a,b=map(int,input().split())
    ans.append([a,b,a-b])
s=0
for i in range(len(ans)):
    s=s+ans[i][0]
m=[]
for i in range(len(ans)):
    m.append(ans[i][2])
m.sort(reverse=True)
if s<=money:
    print(0)
elif s-sum(m)>money:
    print(-1)
else:
    c=0
    for i in range(len(m)):
        c+=1
        s=s-m[i]
        if s<=money:
            break
    print(c)
