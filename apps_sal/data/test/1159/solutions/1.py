import math, sys

def isprime(x):
    for d in range(2, int(math.sqrt(x)) + 1):
        if x % d == 0:
            return False
    return True

n = int(input())

edges = []
for x in range(n):
    edges.append((x, (x + 1) % n))

m = n
i = 0
while not isprime(m):
    edges.append((i, n - 2 - i))
    i += 1
    m += 1

print(m)
for u, v in edges:
    print(u + 1, v + 1)



