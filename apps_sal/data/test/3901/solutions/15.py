def gcd(a,b):
    return b if a==0 else gcd(b%a,a)

def fun():
    if r :
        return n-r
    for i in range(1,n):
        for j in range(n):
            if j+i>=n :
                break
            a[j]=gcd(a[j],a[j+1])
            if a[j]==1:
                return i+n-1
    return -1

n=int(input())
a=list(map(int,input().split()))
r = 0
for i in range(n) :
    if a[i]==1:
        r+=1
print(fun())

