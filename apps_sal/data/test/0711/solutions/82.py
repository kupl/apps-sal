import collections,sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N,M = LI()
ans = 1
def prime_factor(num):
    prime_factor = collections.defaultdict(int)
    for i in range(2,int(num**0.5)+1):
        while num%i==0:
            prime_factor[i] += 1
            num //= i
    if num>1:
        prime_factor[num]=1
    return prime_factor
def nCr(n,r,mod):
    comb_count = 1
    for i in range(r):
        comb_count *= n-i
        comb_count %= mod
    for i in range(1,r+1):
        comb_count *= pow(i,mod-2,mod)
        comb_count %= mod
    return comb_count
for v in list(prime_factor(M).values()):
    ans *= nCr(v+N-1,v,10**9+7)
    ans %= 10**9+7
print(ans)

