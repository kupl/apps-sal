import math
N,M=map(int,input().split())
def C(x):
    if x>=2:
        return math.factorial(x)//(math.factorial(x-2)*2)
    else:
        return 0
print(C(N)+C(M))
