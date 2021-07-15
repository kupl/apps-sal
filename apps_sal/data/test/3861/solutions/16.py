n=int(input())
a=list(map(int,input().strip().split(' ')))
ans=-10000000
for i in a:
    if i<0:
        if i>ans:
            ans=i
    else:
        if int(i**0.5)**2!=i and i>ans:
            ans=i
print(ans)
