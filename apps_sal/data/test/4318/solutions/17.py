n=int(input())
h=list(map(int,input().split()))
ans=1
for i in range(1,n):
    for j in range(0,i):
        if h[i]-h[j]<0:
            break
    else:
        ans+=1
print(ans)
