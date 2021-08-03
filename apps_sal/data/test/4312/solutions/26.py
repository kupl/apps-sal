import math
A, B, C, D = map(int, input().split())
if math.ceil(A / D) >= math.ceil(C / B):
    print('Yes')
else:
    print('No')
