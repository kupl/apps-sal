n = int(input())
ans = 0
for i in range(2,(int(n**0.5))+1):
    x = i
    while n%x==0:
        n = n//x
        x*=i
        ans+=1
    while n%i==0:
        n = n//i
if n!=1:
    ans+=1
print(ans)
