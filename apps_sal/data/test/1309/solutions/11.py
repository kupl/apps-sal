import itertools
n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=10000000
for i in range(2*n):
    for j in range(i+1,2*n):
        x=0
        b=a+[]
        del b[i],b[j-1]
        for k in range(0,2*(n-1),2):
            x+=abs(b[k]-b[k+1])
        if x<ans:
            ans=x
print(ans)
            

