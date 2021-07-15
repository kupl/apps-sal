from collections import deque
import sys

def max(a,b):
    if a>b:
        return a
    else:
        return b

def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [A[i+1]-A[i] for i in range(N-1)]
    S = 0
    for i in range(N-1):
        if A[i+1]>A[i]:
            S += A[i+1] - A[i]
    if (A[0]+S)%2==0:
        print((A[0]+S)//2)
    else:
        print((A[0]+S+1)//2)

    Q = int(input())
    for i in range(Q):    
        L,R,X = list(map(int,input().split()))

        L,R = L-1,R-1

        if L>0:
            temp = B[L-1]
            B[L-1] += X
            S = S - max(0,temp) + max(0,B[L-1])
        else:
            A[0] += X
        if R<N-1:
            temp = B[R]
            B[R] -= X
            S = S - max(0,temp) + max(0,B[R])

        if (A[0]+S)%2==0:
            print((A[0]+S)//2)
        else:
            print((A[0]+S+1)//2)
            
def __starting_point():
    main()



__starting_point()
