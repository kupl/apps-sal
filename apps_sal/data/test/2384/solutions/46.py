import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()

def odd(A):
    oddi=np.array(A[::2],dtype=np.int64)
    eveni=np.array(A[1::2],dtype=np.int64)
    left=np.cumsum(oddi[:-1]-eveni)
    left=np.insert(left,0,0)
    right=np.cumsum(oddi[:0:-1]-eveni[::-1])[::-1]
    right=np.append(right,0)
    tmp=np.max(np.maximum.accumulate(left)+right)
    return tmp+np.sum(eveni)

def even(A):
    left=np.array([0]+A[::2],dtype=np.int64)
    right=np.array(A[1::2]+[0],dtype=np.int64)[::-1]
    return np.max(left.cumsum()+right.cumsum()[::-1])

def main():
    n=int(input())
    A=list(map(int, input().split()))
    if n%2==1:
        print(odd(A))
    else:
        print(even(A))


def __starting_point():
    main()
__starting_point()
