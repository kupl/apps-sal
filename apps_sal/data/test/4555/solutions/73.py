a,b,k=map(int,input().split())
ans=[]
num_min=a+k
num_max=b-k+1
if (b-a+1)>2*k:
    for i in range(a,num_min):
        ans.append(i)
    for i in range(num_max,b+1):
        ans.append(i)
else:
    for i in range(a,b+1):
        ans.append(i)
ans=sorted(set(ans))
for i in ans:
    print(i)
