import math
A, B = map(int, input().split())
 
# A*x-(x-1) >= B
# (A-1)*x >= B-1
# x >= ceil((B-1)/(A-1))
print(math.ceil((B-1)/(A-1)))
