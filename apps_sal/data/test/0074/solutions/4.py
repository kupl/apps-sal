import math
def is_prime(a):
    n=math.sqrt(a)
    n=int(n)+1
    return all(a % i for i in range(2, n))
def sieves(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]
pri=sieves(1000)
n=int(input())
for i in range(n,1,-1):
    if is_prime(i):
        primes=i
        break

ans=[]
no=1
if n==primes:
    ans=[n]
    no=1

elif primes+2==n:
    ans=[2,primes]
    no=2
else:
    k=n-primes
    for i in pri:
        for j in pri:
            if i+j==k:
                ans=[primes,i,j]
                no=3
print(no)
for i in ans:
    print(i,end=' ')
