n=int(input())
a=sorted(list(map(int,input().split())))
ans=a.pop()
for i in range(n//2-1):
    ans+=2*a.pop()
if n%2==1:
    ans+=a.pop()
print(ans)
