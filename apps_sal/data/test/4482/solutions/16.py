n=int(input())
a=[int(i) for i in input().split()]

ans=10000000000000000
for criterion in range(-100,101):
    result=0
    for i in a:
        result+=(i-criterion)**2
    ans=min(ans,result)
print(ans)
