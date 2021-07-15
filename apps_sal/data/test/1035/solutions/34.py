import itertools
import sys
a,b=list(map(int,input().split()))

# 最大公約数（ユークリッドの互除法）
def gcd(A,B):
    while B!=0:
        A,B=B,A%B
    return A

# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5)+1):
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

print((len(factorization(gcd(a,b)))+1 if a!=1 and b!=1 else 1))
# print(gcd(a,b))
# print(factorization(gcd(a,b)))

