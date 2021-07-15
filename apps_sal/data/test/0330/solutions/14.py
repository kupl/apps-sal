def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    ls=[]
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            ls.append(p)
    return ls
ls=SieveOfEratosthenes(100000)
p,y=[int(i) for i in input().split(" ")]
while (y!=p):
    flag=0
    for i in ls:
        if i>p:
            break
        if not y%i:
            flag=1
            break
    if not flag:
        print(y)
        return
    y-=1
print(-1)
