N=int(input())

h=list(map(int,input().split()))
sw=True
temp=0
ans=0
for i in range(N-1):
    if sw==True:
        if h[i]>h[i+1]:
            ans+=h[i]-temp
            sw=False
    else:
        if h[i]<h[i+1]:
            temp=h[i]
            sw=True
if sw==True:
    ans+=h[N-1]-temp

print(ans)

