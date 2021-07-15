import math
from functools import reduce
n, m = map(int, input().split())
A = list(map(int, input().split()))

a0 = A[0]
cnt = 0
while a0%2 == 0:
    a0 //= 2
    cnt += 1

a = []
for aa in A:
    if cnt == 1:
        if aa%4 == 0:
            print(0)
            return
    else:
        if aa%(2**(cnt-1)) != 0 or aa%(2**cnt) != 0 or aa%(2**(cnt+1)) == 0:
            print(0)
            return
    a.append(aa//2)


def lcm_base(p, q):
    return (p * q) // math.gcd(p, q)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


lcm = lcm_list(a)
print(m//lcm - m//(lcm*2))
