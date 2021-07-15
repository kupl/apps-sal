import numpy as np
from numpy.fft import rfft,irfft
import sys
sys.setrecursionlimit(10**9)

def mi(): return list(map(int,input().split()))
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print(("-------\n{}\n-------".format(text)))

INF=10**20
class Polynomial:
    def __init__(self,dim=0,const=1):
        self.values = [(dim,const)]
    def __add__(self,other):
        return self.values + other.values


class PolySolver:
    def __init__(self,size,init_val=1):
        self.size = size
        self.f = np.zeros(size, np.int64)
        self.f[0] = init_val


    def multiple(self,polynomial,MOD): # const1 * x^dim1 + const2 * x^dim2 + ... をfにかけ合わせる
        new_F = np.zeros(self.size, np.int64)
        for dim,const in polynomial:
            if dim != 0:
                g = np.zeros(self.size, np.int64)
                g[dim:] += self.f[:-dim] # dim分係数情報をずらす
            else:
                g = const * self.f.copy()

            new_F += g

        self.f = new_F
        
    
    def add(self,polynomial): # const1 * x^dim1 + const2 * x^dim2 + ... をfに足す
        for dim,const in polynomial:
            self.f[dim] += const
            

    def get_coefficient(self,dim):
        return self.f[dim]

    def fft(self,A,B,fft_len=1<<18):
        x = irfft(rfft(A,fft_len) * rfft(B,fft_len))
        return np.rint(x).astype(np.int64)

    def convolve(self,g):
        h = self.fft(self.f,g)[:len(self.f) + len(g) - 1]
        self.f = h
    


def main():
    N,M=mi()
    A=list(mi())
    
    mx = 2*10**5+10
    F = PolySolver(mx,init_val=0)
    for a in A:
        F.add(Polynomial(dim=a).values)
    
    g = F.f
    F.convolve(g)

    ans = 0
    handshake = M
    for x in range(mx-1,1,-1):
        count = F.get_coefficient(x)
        if count <= 0: continue

        if count > handshake:
            ans += handshake * x
        else:
            ans += count * x
 
        handshake = max(handshake-count,0)
        if handshake == 0:
            break

    print(ans)

def __starting_point():
    main()

__starting_point()
