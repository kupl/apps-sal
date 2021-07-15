x,n=map(int,input().split())
p=list(map(int,input().split()))
temp=100
for i in range(x-51,x+51):
    a=abs(x-i)
    if a<temp and i not in p:
        temp=a
        ans=[i]
    if a==temp and i not in p:
        ans+=[i]
print(min(ans))
