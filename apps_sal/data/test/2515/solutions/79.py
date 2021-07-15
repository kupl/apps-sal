from math import floor, sqrt
def __starting_point():
    Q = int(input())
    acc = [0]*(10**5+1)
    primes = set([2])
    for i in range(3,10**5+1):
        fl = True
        for j in range(2, floor(sqrt(i))+1):
            if i % j == 0:
                fl = False
                break
        acc[i] = acc[i-1]
        if fl:
            primes.add(i)
            if (i+1)//2 in primes:
                acc[i] += 1
    for q in range(Q):
        l, r = map(int,input().split())
        print(acc[r]-acc[l-1])
__starting_point()
