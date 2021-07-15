def mp():  return list(map(int,input().split()))
def lt():  return list(map(int,input().split()))
def pt(x):  print(x)
def ip():  return input()
def it():  return int(input())
def sl(x):  return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x):  return "{0:b}".format(x)
def printlist(l): print(' '.join([str(x) for x in l]))
def listring(l): return ''.join([str(x) for x in l])

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 10:
        return True
    p = 5
    while p <= int(n**0.5):
        if n % p == 0 or n % (p+2) == 0:
            return False
        p += 6
    return True
n = it()
if isPrime(n):
    print(1)
    print(n)
elif isPrime(n-2):
    print(2)
    print("2 %d" % (n-2))
else:
    r = 4
    while not isPrime(n-r):
        r += 2
    if r == 4:
        p,q = 2,2
    elif r == 6:
        p,q = 3,3
    elif r == 8:
        p,q = 3,5
    elif r == 10:
        p,q = 5,5
    elif r == 12:
        p,q = 5,7
    else:
        if isPrime(r-3):
            p,q = 3,r-3
        else:
            p = 5
            while not (isPrime(r-p) and isPrime(p)) and not (isPrime(r-p-2) and isPrime(p+2)):
                p += 6
            if isPrime(p) and isPrime(r-p):
                p,q = p,r-p
            else:
                p,q = p+2,r-p-2
    print(3)
    print("%d %d %d" % (n-r,p,q))


