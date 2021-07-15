n,T=list(map(int,input().split()))
c=[0]*n
t=[0]*n
ans=[]
for i in range(n):
    c[i],t[i]=list(map(int,input().split()))
    if t[i]<=T:
        ans.append(c[i])
if len(ans)==0:
    print("TLE")
    return
print((min(ans)))

