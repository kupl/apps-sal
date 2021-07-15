from math import sqrt; from itertools import count, islice

# def isPrime(n,p):
#     for i in range(2,)
#     return n > 1 and all(n%i for i in islice(count(2), int(sqrt(p))))


def isPrime(n,p) :
    j=int(sqrt(n))
    if p*p < n:
        j=p
   # Check from 2 to n-1
    for i in range(2, j+1):
        if n % i == 0:
            return False
    return True

    # # This is checked so that we can skip
    # # middle five numbers in below loop
    # if (n % 2 == 0 or n % 3 == 0) :
    #     return False
    #
    # i = 5
    # while(i * i <= n) :
    #     if (n % i == 0 or n % (i + 2) == 0) :
    #         return False
    #     i = i + 6
    #
    # return True

p,y=list(map(int,input().split(' ')))
flag=0
for i in range(y,p,-1):
    if isPrime(i,p):
        print(i)
        flag=1
        break
if flag==0:
    print(-1)

