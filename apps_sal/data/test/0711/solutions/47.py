import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,m = list(map(int,ipt().split()))
    d = dict()
    mod = 10**9+7
    p = primes(m)
    for i in p:
        t = 0
        while True:
            if m%i == 0:
                m //= i
                t += 1
            else:
                break
        if t > 0:
            d[i] = t
        if i > m:
            break
    if m > 1:
        d[m] = 1
    ans = 1

    #nCrをmodで割った余りを求める。Nに最大値を入れて使用。
    N = 10**5+1000
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    def cmb(n,r,mod):
        if r<0 or r>n :
            return 0
        r = min(r,n-r)
        return g1[n]*g2[r]*g2[n-r]%mod
    for i in range(2,N+1):
        g1.append((g1[-1]*i)%mod)
        inverse.append((-inverse[mod % i]*(mod//i))%mod)
        g2.append((g2[-1]*inverse[-1])%mod)

    for i in list(d.values()):
        ans = (ans*cmb(n-1+i,i,mod))%mod

    print(ans)

    return

#√nまでの素数の配列を返す関数
def primes(n):
    if n < 4:
        return []
    else:
        pri = [2]
        k = 3
        while k*k <= n:
            for i in pri:
                if k%i == 0:
                    break
                elif i == pri[-1]:
                    pri.append(k)
            k += 2
        return pri

def __starting_point():
    main()

__starting_point()
