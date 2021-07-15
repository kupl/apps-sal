import math
def f(n):
    l = math.factorial(n)*n
    ans = l * (l-n+2) // 2
    for i in range(1,n):
        ans -= math.factorial(n)//math.factorial(i+1)*n*(i*(n-i)-1)
    return ans

def solve(n):
    M = 998244353
    p = n
    a = 0
    for i in range(n,1,-1):
        a=(a+p*(i-1)*(n-i+1)-p)%M
        p=p*i%M
    a = (p*(p-n+2)-2*a)%M
    if a&1:a+=M
    return a//2

x = int(input())
ans = solve(x)
print(ans)
