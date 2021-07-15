x,y,z=list(map(int,input().split()))

ans = 0

for i in range(x):
    
    if y*i+z*(i+1) <= x:
        ans=max(ans, i)
print(ans)

