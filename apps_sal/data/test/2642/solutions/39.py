N = int(input())
zero = 0
r_zero = 0
l_zero = 0
mod = 1000000007
from collections import defaultdict
from math import gcd
dic = defaultdict(int)
for i in range(N):
    A, B = list(map(int, input().split()))
    if A==0 and B==0:
        zero += 1
        continue
    elif A==0:
        r_zero += 1
    elif B==0:
        l_zero += 1
    else:
        g = gcd(A, B)
        A //= g
        B //= g
        if A<0:
            A, B = -A, -B
        dic[(A, B)] += 1

dickey = list(dic.keys())
s = set(dickey)
nopair = N-zero-r_zero-l_zero
ans = pow(2, r_zero, mod)+pow(2, l_zero, mod)-1
for a, b in dickey:
    if a*b>0 and (b, -a) in s:
        ans *= (pow(2, dic[(a, b)], mod)+pow(2, dic[(b, -a)], mod)-1)%mod
        nopair -= (dic[(a, b)]+dic[(b, -a)])
ans *= pow(2, nopair, mod)
print(((ans-1+zero)%mod))


