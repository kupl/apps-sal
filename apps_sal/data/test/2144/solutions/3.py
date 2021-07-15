primes=[True]*1000001
primes[0]=False
primes[1]=False
for i in range(2, 100001):
    if primes[i]:
        for j in range(i*2, 100001, i):
            primes[j]=False
pL=[]
for i in range(2, 100001):
    if primes[i]:pL.append(i)
def fact(n):
    L=[]
    for i in pL:
        if n%i==0:
            while n%i==0:
                L.append(i)
                n//=i
    if n!=1:L.append(n)
    return L
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
for i in ' '*int(input()):
    a,m=map(int,input().split())
    g=gcd(a,m)
    aa=a//g
    mm=m//g
    L=fact(mm)
    M=[]
    for i in L:
        if i not in M:M.append(i)
    for i in M:
        mm*=(i-1)
        mm//=i
    print(mm)
