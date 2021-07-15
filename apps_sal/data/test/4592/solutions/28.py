import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

def primeFactorization(n, primes):
    ans = []
    temp = n
    for p in primes:
        while temp%p == 0:
            ans.append(p)
            temp //= p
    if temp > 1:
        ans.append(temp)
    return collections.Counter(ans)

def resolve():
    N = I()

    primes = sieve(N)
    cnt = collections.Counter()
    
    for i in range(2, N + 1):
        pf = primeFactorization(i, primes)
        for k, v in list(pf.items()):
            cnt[k] += v

    ans = 1
    for i in list(cnt.values()):
        ans *= (i + 1)
        ans %= MOD

    print(ans)

def __starting_point():
    resolve()

__starting_point()
