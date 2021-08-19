import math
n = int(input())
A = []
for i in range(5):
    A.append(int(input()))
minA = min(A)
print(4 + math.ceil(n / minA))
