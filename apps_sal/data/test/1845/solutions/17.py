from collections import deque, Counter, OrderedDict
from heapq import nsmallest, nlargest
from math import ceil,floor,log,log2,sqrt,gcd,factorial
def binNumber(n,size=1):
    return bin(n)[2:].zfill(size)

def iar():
    return list(map(int,input().split()))

def ini():
    return int(input())

def isp():
    return list(map(int,input().split()))

def sti():
    return str(input())

def par(a):
    return ' '.join(list(map(str,a)))

class pair:
    def __init__(self,f,s):
        self.fi = f
        self.se = s
    def __lt__(self,other):
        return (self.fi,self.se) < (other.fi,other.se)

#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|  
#  code

def __starting_point():
    n = ini()
    a = iar()
    mi = min(a)
    mis = sum(a)
    mas = mis
    for i in a:
        if i == mi:
            continue
        j = 2
        while j*j <= i:
            if i%j == 0:
                c1 = i//j
                c2 = mi*j
                x = mas - mi - i + c1 + c2
                if x < mis:
                    mis = x
                if j != i//j:
                    k = i//j
                    c1 = i//k
                    c2 = mi*k
                    x = mas + c1 + c2 - mi - i
                    if x < mis:
                        mis = x
            j += 1
    print(mis)

__starting_point()
