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
    def __init__(self,coefficient=None,dim=0,const=1):
        if coefficient == None:
            self.coefficient = np.zeros(dim+1, np.int64)
            self.coefficient[dim] = const
        else:
            self.coefficient = coefficient

    def __add__(self,other): # +
        f,g = self.coefficient, other.coefficient
        if len(f) > len(g): f,g = g,f

        h = Polynomial(dim=len(g)-1,const=0)
        h.coefficient[len(f):] += g[len(f):]
        h.coefficient[:len(f)] += f + g[:len(f)]
        return h
    
    def __iadd__(self,other): # +=
        h = self.__add__(other)
        self.coefficient = h.coefficient
        return self

    def __mul__(self,other): # *
        f = self.coefficient
        g = other.coefficient
        h = Polynomial()
        h.coefficient = self.fft(f,g)[:len(f)+len(g)-1]
        return h
    
    def __len__(self):
        return len(self.coefficient)

    def __getitem__(self,key):
        return self.coefficient[key]

    def get_coefficient(self,x):
        return self.coefficient[x]


    def fft(self,A,B,fft_len=1<<18):
        x = irfft(rfft(A,fft_len) * rfft(B,fft_len))
        return np.rint(x).astype(np.int64)



def main():
    N,M=mi()
    A=list(mi())
    
    coefficient = [0] * (2*10**5+10)
    for a in A:
        coefficient[a] += 1
    
    f = Polynomial(coefficient=coefficient)
            
    g = f * f
    ans = 0
    handshake = M
    for x in range(len(g)-1,1,-1):
        count = g[x]
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
