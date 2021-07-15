import numpy as np
from numpy.fft import rfft,irfft
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
class Counter:
    def __init__(self):
        self.dict = {}

    def add(self,x):
        if x in self.dict: self.dict[x] += 1
        else: self.dict[x] = 1

    def decrement(self,x):
        self.dict[x] -= 1
        if self.dict[x] <= 0:
            del self.dict[x]

    def get_dict(self):
        return self.dict




def fft(A,B,fft_len=2*10**5):
    x = irfft(rfft(A,fft_len) * rfft(B,fft_len))+0.5
    return x.astype(int)


def main():
    N,M=mi()
    A=list(mi())

    counter = Counter()
    for a in A: 
        counter.add(a)
    
    count_map = counter.get_dict()
    F=[0]*2*10**5
    for a,count in count_map.items():
        F[a] = count
    
    G = fft(F,F,fft_len=1<<18)

    ans = 0
    handshake = M
    for x in range(len(G)-1,1,-1):
        if G[x] <= 0: continue
        count = G[x]
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
