def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

n = int(input())
if n==1:
    print(1)
elif n==2:
    print(2)
elif n%2 == 1:
    print(lcm(n,lcm(n-2,n-1)))
else :
    ans = 0
    for i in range(max(n-50,1),n+1) :
        for j in range(max(n-50,1),n+1) :
            for k in range(max(n-50,1),n+1) :
                ans = max(ans,lcm(i,lcm(j,k)))
    print(ans)
