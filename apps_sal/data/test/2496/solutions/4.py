#高速素因数分解  osa_k法 
def osa_k(a):
    tmp = set()
    while a > 1:
        tmp.add(sieve[a])
        a //= sieve[a]
    return tmp

    # 初期入力
import math
import sys
from bisect import bisect_left
from functools import reduce
input = sys.stdin.readline  #文字列では使わない
N = int(input())
A = list(map(int, input().split()))
used =set()

#not coprimeの判定
gcd_a =reduce(math.gcd,A)
if gcd_a !=1:
    ans ="not coprime"

#pairwise coprimeの判定
else:
    MAXN =10**6 +10
    #osa_k法
    sieve = [i for i in range(MAXN+1)]
    p = 2
    while p*p <= MAXN:
        if sieve[p] == p:
            for q in range(2*p,MAXN+1,p):
                if sieve[q] == q:
                    sieve[q] = p
        p += 1
    
    ans ="pairwise coprime"
    for a in A:
        aa =osa_k(a)
        if used & aa:
            ans ="setwise coprime"
            break #共通要素があったらpair_wではない→set_w
        used |=aa
    
print(ans)
