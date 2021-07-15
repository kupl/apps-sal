import math
import bisect

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)



def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


primes = []

def isprime(n):
    for d in range(2, int(math.sqrt(n))+1):
        if n%d==0:
            return False
    return True


def argsort(ls):
    return sorted(range(len(ls)), key=ls.__getitem__)

def f(p=0):
    if p==1:
        return map(int, input().split())
    elif p==2:
        return list(map(int, input().split()))
    else:
        return int(input())

n = f()
cl = f(2)

a = cl.count(1)
b = cl.count(0)

for i in range(n):
    if cl[i]==0:
        b-=1
    else:
        a-=1

    if a==0 or b==0:
        print(i+1)
        break
