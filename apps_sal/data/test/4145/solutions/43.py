X = int(input())

def isPrime(n):
    if n <= 1:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True

for x in range(X,1000004):
    if isPrime(x):
        print(x)
        return
