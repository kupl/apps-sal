import math
N = int(input().rstrip())
A = int(input().rstrip())
B = int(input().rstrip())
C = int(input().rstrip())
D = int(input().rstrip())
E = int(input().rstrip())
print(math.ceil(N / min(A, B, C, D, E)) + 4)
