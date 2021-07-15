def GCD(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def gcd_all(a):
    n = len(a)
    gcd = a[0]
    for i in range(1, n):
        gcd = GCD(gcd, a[i])
    return gcd

def f(a):
    mx = 10**6
    p = set([])
    sieve = [i for i in range(mx + 1)]
    for i in range(2, int(mx**0.5 + 1)):
        for j in range(2 * i, mx + 1, i):
            if sieve[j] > i:
                sieve[j] = i
    pairwise_coprime = True
    for i in a:
        p2 = set([])
        while i > 1:
            p2.add(sieve[i])
            i //= sieve[i]
        for j in p2:
            if j in p:
                pairwise_coprime = False
                break
            p.add(j)
        if pairwise_coprime == False:
            break
    gcd = gcd_all(a)
    if pairwise_coprime == False and gcd == 1:
        return 'setwise coprime'
    elif pairwise_coprime:
        return 'pairwise coprime'
    else:
        return 'not coprime'

n = int(input())
a = list(map(int, input().split()))
print((f(a)))

