N=int(input())
A=list(map(int,input().split()))

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

ans=A[0]
for i in range(1,N):
    ans=gcd(ans,A[i])
print(ans)
