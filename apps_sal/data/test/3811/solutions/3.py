import math


def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.append(i)
            n = n // i
    if n > 2:
        l.append(n)
    return list(set(l))


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


n = int(input())
c = 0
a, b = [int(x) for x in input().split()]

# if is_prime(a) and is_prime(b):
#    c+=1
l1, l2 = primeFactors(a), primeFactors(b)
d = list(set(l1 + l2))
f = 0
for i in range(1, n):
    a, b = [int(x) for x in input().split()]
    # if is_prime(a) and is_prime(b):
    #    c+=1
    s = []
    for p in d:
        if a % p != 0 and b % p != 0:
            s.append(p)
    for ele in s:
        d.remove(ele)
    # print(d)
    if len(d) == 0:
        f = 1
        ans = -1
        break
if f != 1:
    ans = d[0]
print(ans)
