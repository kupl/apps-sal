'''
import sys
def Calc(N):
    return(N*((N+1)*.5))
N=int(input())
C=0
for I in range(1000000000000000000):
    C+=Calc(I)
    if C==N:
        print(I)
        return
    elif C>N:
        print(I-1)
        return
'''
A = list(map(int, input().split()))
L = list(map(int, input().split()))
L.append(-(min(L)))
L.sort()


def Fasl(Array):
    Out = 0
    for I in range(len(Array) - 1):
        if Array[I + 1] - Array[I] > Out:
            Out = Array[I + 1] - Array[I]
    return Out


fasl = Fasl(L) / 2
If = A[1] - max(L)
if If > fasl:
    print(If)
else:
    print(fasl)
