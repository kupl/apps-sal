import math

n = int(input())

def s(n, k):
    count = n//k
    return k*count*(count-1)//2 + count

result = []

for d in range(1, int(math.sqrt(n))+1):
    if n%d != 0:
        continue
    d2 = n//d
    result.append(s(n, d))
    if d2 != d:
        result.append(s(n, d2))

result.sort()

print(*result)

