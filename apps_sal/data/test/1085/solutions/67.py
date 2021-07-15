import sys
from math import gcd

N = int(input())
if N == 2:
    print((1))
    return

"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])

    return arr


factors = factorization(N)
ans = 0

# K^i
tmp = factors[0][1]
for k, i in factors:
    tmp = gcd(tmp, i)
ptn = 1
if tmp != 1:
    for k, i in factorization(tmp):
        ptn *= i+1
ans += ptn

# ak+1
ptn = 1
for k, i in factorization(N-1):
    ptn *= i+1
ptn -= 1  # k=1のときを除外
ans += ptn

# (ak+1)*k^i
ptn = 0
for f, n in factors:
    for i in range(1, n+1):
        k = f**i
        tmp = N
        while True:
            if tmp%k!=0:
                break
            tmp = tmp/k
        ptn += ((tmp-1)%k==0 and tmp!=1)
ans += ptn

print(ans)

