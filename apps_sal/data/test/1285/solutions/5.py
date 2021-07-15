from sys import stdin,stdout
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n=int(stdin.readline())
temp=""
ans=n
p=0
for i in range(n):
    s=bin((1<<n)+int(stdin.readline(),16))[3:]
    if i==0 or temp!=s:
        temp=s
        ans=gcd(ans,p)
        p=1
        pp=1
        for j in range(1,n):
            if s[j]==s[j-1]:
                pp+=1
            else:
                ans=gcd(ans,pp)
                pp=1
    else:
        p+=1
ans=gcd(ans,p)
print(ans)
