def fact(n):
    rest = 1
    for i in range(1,n+1):
        rest *= i
    return rest
 
def f(n):
    l = fact(n) * n
    ans = l * (l-n+2) // 2
    for i in range(1,n):
        ans -= fact(n) // fact(i+1) * n * (i * (n-i) - 1)
    return ans
 
#print(f(int(input())) % 998244353)
 
def g(n):
    M = 998244353
    p = n
    a = 0
    for i in range(n,1,-1):
        a=(a+p*(i-1)*(n-i+1)-p)%M
        p=p*i%M
    a=(p*(p-n+2)-a-a)%M
    if a&1:a+=M
    return a//2
 
print(g(int(input())))

