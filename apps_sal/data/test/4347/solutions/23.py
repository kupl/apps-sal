def fact(n) :
    ans = 1
    for i in range(2,n+1) : ans *= i
    return ans
n = int(input())//2 - 1
print(fact(2*n + 1)//(n + 1))


