import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    a,b = list(map(int,ipt().split()))
    if a == 1 and b == 1:
        print((1,2))
        print(".#")
        return()
    print((100,100))
    a -= 1
    b -= 1
    ni = 0
    while a >= 50:
        print((".#"*50))
        print(("#"*100))
        ni += 2
        a -= 50
    print((".#"*a+"##"*(50-a)))
    print(("#"*100))
    ni += 2
    for i in range(50-ni):
        print(("#"*100))
    ni = 0
    while b >= 50:
        print(("."*100))
        print((".#"*50))
        ni += 2
        b -= 50
    print(("."*100))
    print((".#"*b+".."*(50-b)))
    ni += 2
    for i in range(50-ni):
        print(("."*100))



    return

def __starting_point():
    main()

__starting_point()
