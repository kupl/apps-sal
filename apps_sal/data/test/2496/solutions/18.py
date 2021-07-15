n = int(input())
a = list(map(int, input().split()))
MAX_A = max(a)
divide_minimam_prime = [i for i in range(MAX_A + 1)]
is_prime = [True for i in range(MAX_A + 1)]
is_prime[0] = False
is_prime[1] = False
for div in range(2,int(MAX_A**0.5) + 1):
    if is_prime[div]:
        # divが素数だった場合
        k = div
        divide_minimam_prime[k] = k
        k += div
        while k <= MAX_A:
            is_prime[k] = False
            if divide_minimam_prime[k] == k:
                divide_minimam_prime[k] = div
            k += div
# pairwise coprimeであるかどうか？
pairwise_coprime = True
use_divnum = set()
for i in range(n):
    k = a[i]
    while k != 1:
        if divide_minimam_prime[k] in use_divnum:
            pairwise_coprime = False
            break
        else:
            use_divnum.add(divide_minimam_prime[k])
        div = divide_minimam_prime[k]
        while k % div == 0 and k > 1:
            k = k // div
if pairwise_coprime: 
    print("pairwise coprime")
    return
from math import gcd
gcd_of_a = a[0]
for i in range(n):
    gcd_of_a = gcd(gcd_of_a, a[i])
if gcd_of_a == 1:
    print("setwise coprime")
else:
    print("not coprime")
