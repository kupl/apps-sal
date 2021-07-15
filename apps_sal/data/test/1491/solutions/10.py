n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    s=i**0.5
    s=round(s)
    x.append((abs(s**2-i),i))

x.sort()
n2=n//2
ans=0
for i in range(n2):
    ans+=x[i][0]
for i in range(n2,n):
    if x[i][0]==0:
        if x[i][1]==0:
            ans+=2
        else:
            ans+=1
print(ans)

