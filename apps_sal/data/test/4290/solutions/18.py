def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def combination(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))

N,M = map(int,input().split())

print(combination(N,2)+combination(M,2))
