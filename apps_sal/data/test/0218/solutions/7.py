import math

def euclid_algorithm(a, b):
    t1, t2 = abs(a), abs(b)
    #saving equalities:
    #t1 == x1 * a + y1 * b,
    #t2 == x2 * a + y2 * b. 
    x1, y1, x2, y2 = int(math.copysign(1, a)), 0, 0, int(math.copysign(1, b))
    if t1 < t2:
        t1, t2 = t2, t1
        x1, y1, x2, y2 = x2, y2, x1, y1

    while t2 > 0:
        if x1 * a + y1 * b != t1:
            print('inshalla')
        k = int(t1 // t2)
        t1, t2 = t2, t1 % t2
        #t1 - k * t2 == (x1 - k * x2) * a + (y1 - k * y2) * b
        x1, y1, x2, y2 = x2, y2, x1 - k * x2, y1 - k * y2

    return t1, x1, y1

def opposite_element(x, p):
    gcd, k, l = euclid_algorithm(x, p)
    if gcd != 1:
        return -1
    return k % p

def fact_mod(n, p):
    prod = 1
    for i in range(2,n+1):
        prod *= i
        prod %= p
    return prod

n, p, q = [int(x) for x in input().split()]
s = input().rstrip()
for i in range(n // p + 1):
    if (n - p*i) % q == 0:
        j = (n - p*i) // q
        print(i+j)
        for k in range(i):
            print(s[k*p:(k+1)*p])
        for k in range(j):
            print(s[p*i + k*q: p*i + (k+1)*q])
        break
else:
    print(-1)
    

