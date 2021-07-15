MOD = 1000000007
def phi(n):
    res = n
    for i in range(2,int(n**(0.5)+1)):
        if n % i == 0:
            while n % i == 0:
                n = n//i
            res -= res//i
    if n > 1:
        res -= res//n
    return res

n,k = list(map(int,input().split()))
k = (k+1)//2
ans = n
for _ in range(k):
    if ans > 1:
        ans = phi(ans)
    else:
        break
print(ans % MOD)

