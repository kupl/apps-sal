n=int(input())
a=[int(input()) for _ in range(n)]
light=0
ans=0
for i in range(n):
    if a[light]==2:
        ans+=1
        break
    else:
        light=a[light]-1
        ans+=1
else:
    ans=-1
print(ans)
