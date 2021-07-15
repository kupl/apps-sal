import numpy as np
import bisect
def sieve_of_eratosthenes(n):
    max = int(np.sqrt(n))
    seachList = [i for i in range(2,n+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        prm = seachList[0]
        seachList = [i for i in seachList if i%prm != 0]
    primeNum.extend(seachList)
    return primeNum


Q = int(input())
l = []
r = []
for i in range(Q):
    a,b = list(map(int,input().split()))
    l.append(a)
    r.append(b)

prime_list = sieve_of_eratosthenes(max(r))

ruiseki = [0]*len(prime_list)
for i in range(len(prime_list)):
    if (prime_list[i]+1)//2 in prime_list:
        ruiseki[i] += 1 + ruiseki[i-1]
    else:
        ruiseki[i] = ruiseki[i-1]

ruiseki.insert(0,0)

for i in range(Q):
    ans = 0
    ans = ruiseki[bisect.bisect_right(prime_list,r[i])] - ruiseki[bisect.bisect_left(prime_list,l[i])]
    print(ans)

