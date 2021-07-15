#!/usr/bin/env python3
import sys
from networkx.utils import UnionFind
from operator import itemgetter
def input(): return sys.stdin.readline().rstrip()

class prepere_pch:
    def __init__(self, maxnum=3*10**5, mod=10**9+7):
        self.factorial = [0]*(maxnum+1)
        self.factorial[0] = 1
        for i in range(1, maxnum):
            self.factorial[i] = (self.factorial[i-1]*i) % mod
        self.mod = mod
    def per(self,n,r):
        return (self.factorial[n]*pow(self.factorial[n-r],-1,self.mod)) % self.mod

    def com(self,n,r):
        return self.per(n,r)*pow(self.factorial[r],-1,self.mod)
    
    def comH(self,n,r):
        return self.com(n+r-1,r)

def main():
    n,m,k=list(map(int, input().split()))
    ans=0
    pt=m
    pch=prepere_pch(mod=998244353)
    for same in range(n-1,-1,-1):
        if same <=k:
            ans+=pt*pch.com(n-1,same)
            ans%=998244353
        pt*=m-1
        pt%=998244353
    print(ans)


def __starting_point():
    main()

__starting_point()
