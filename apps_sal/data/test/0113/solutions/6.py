n, k = [int(i) for i in input().split()]
t1 = 0
while t1 < k and n % 5 == 0:
    t1 += 1
    n //= 5
t1 = 0
while t1 < k and n % 2 == 0:
    t1 += 1
    n //= 2
print(n * (10**k))
