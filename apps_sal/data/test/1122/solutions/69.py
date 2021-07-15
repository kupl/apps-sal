#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N,M = list(map(int, input().split()))
    i = 1
    for m in range(M):
        if N%2 == 0 and i%2 == 1 and i >= N/2:
            i += 1
        print((M-m,M-m+i))
        i += 2
    

main()

