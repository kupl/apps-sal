import math
n= int(input())
for i in range(n):
    A, B, C, D = [int(s) for s in input().split()] 
    left = A - B
    if left <1:
        print(B)
    else:
        if C > D:
            gone = C - D
            print(B + (math.ceil(left/gone) * C))
        else:
            print(-1)
