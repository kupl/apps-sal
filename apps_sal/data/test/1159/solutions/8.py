def primes(n):
    if(n<=2):
        return []
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int(((n-i*i-1)/(2*i)+1))
    return [2] + [i for i in range(3,n,2) if sieve[i]]
P=primes(2001)


n = int(input())
i = 0
while(P[i] < n):
    i+=1
m = P[i]


toprint = []

for i in range(1, n + 1):
    toprint.append([i, (i) % n + 1])
vis = [False for i in range(n + 1)]
for i in range(1, n + 1):
    if(vis[i]):
        continue
    if(vis[(i + 1)%n + 1]):
        continue
    vis[i] = True
    vis[(i + 1)%n + 1] = True
    toprint.append([i, (i + 1)%n + 1])
print(m)
if(len(toprint) < m):
    print('shit', m, n)
for i in range(m):
    print(*toprint[i])



