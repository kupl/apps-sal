def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 250)]
    p = 2
    while (p * p <= n + 250):
        if (prime[p] == True):
            for i in range(p * p, n + 250, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 250):
        if prime[p] and p >= n:
            print(p)
            break


n = int(input())
SieveOfEratosthenes(n)
