N = 10 ** 6 * 2 
MOD = 1000000007
prime = []
isPrime = [True for i in range(N)]
for i in range(2, N):
    if isPrime[i]:
        prime.append(i)
        for j in range(i * i, N, i):
            isPrime[j] = False
def phi(n):
    ans = 1
    for i in pf(n):
        ans *= pow(i[0],i[1]-1)*(i[0]-1)
    return ans
def pf(n):
    for i in prime:
        cnt = 0
        if n % i == 0:
            while n % i == 0:
                n //= i
                cnt += 1
            yield (i,cnt)
    if n > 1:
        yield (n,1)
n,k = list(map(int,input().split()))
k = (k+1)//2
ans = n
for i in range(k):
    ans = phi(ans)
    if ans == 1:
        break
print(ans % MOD)

