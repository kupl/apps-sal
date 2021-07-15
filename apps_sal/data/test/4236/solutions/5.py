n,m=map(int,input().split())
s=[]
ans=[]
for i in range(n):
    s.append(list(map(int,input().split())))
for i in range(1,m+1):
    t=True
    for j in s:
        if i>=j[0] and i<=j[1]:
            t=False
            break
    if t:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i,end=" ")

