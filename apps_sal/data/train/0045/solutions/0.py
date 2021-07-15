import sys
import random
from fractions import Fraction
from math import *
 
def input():
    return sys.stdin.readline().strip()
 
def iinput():
    return int(input())

def finput():
    return float(input())

def tinput():
    return input().split()

def linput():
    return list(input())
 
def rinput():
    return list(map(int, tinput()))

def fiinput():
    return list(map(float, tinput()))
 
def rlinput():
    return list(map(int, input().split()))
def trinput():
    return tuple(rinput())

def srlinput():
    return sorted(list(map(int, input().split())))

def NOYES(fl):
    if fl:
        print("NO")
    else:
        print("YES")
def YESNO(fl):
    if fl:
        print("YES")
    else:
        print("NO")
    
def main():
    n = iinput()
    #k = iinput() 
    #m = iinput() 
    #n = int(sys.stdin.readline().strip()) 
    #n, k = rinput()
    #n, m = rinput()
    #m, k = rinput()
    #n, k, m = rinput()
    #n, m, k = rinput()
    #k, n, m = rinput()
    #k, m, n = rinput() 
    #m, k, n = rinput()
    #m, n, k = rinput()
    #q = srlinput()
    #q = linput()
    s, t, res = 1, 1, 0
    while s <= n:
        res += 1
        n -= s
        t = 2 * t + 1
        s = (t * (t + 1)) // 2
    print(res)
        
    
                
    
    
    
            
    
        
    

for i in range(iinput()):
    main()

