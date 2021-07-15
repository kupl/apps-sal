l = [0] + list(map(int, input().split()))
from math import sqrt
k = l[6] / sqrt(l[3]**2 + l[4]**2)
A = (l[1] + l[3] * k, l[2] + l[4] * k)
l[3], l[4] = -l[4], l[3]
k = l[5] / (2 * sqrt(l[3]**2 + l[4]**2))
B = (l[1] + l[3] * k, l[2] + l[4] * k)
k = l[7] / (2 * sqrt(l[3]**2 + l[4]**2))
C = (l[1] + l[3] * k, l[2] + l[4] * k)
F = (2 * l[1] - C[0], 2 * l[2] - C[1])
G = (2 * l[1] - B[0], 2 * l[2] - B[1])
L = [l[3], l[4]] 
l[3], l[4] = -l[4], l[3]
R = [-l[4], l[3]]
K = l[7] / (2 * sqrt(l[3]**2 + l[4]**2))
k = l[8] / sqrt(l[3]**2 + l[4]**2)
M = (l[1] + l[3] * k, l[2] + l[4] * k)
D = (M[0] + L[0] * K, M[1] + L[1] * K)
E = (M[0] + R[0] * K, M[1] + R[1] * K)

print(*A)
print(*B)
print(*C)
print(*D)
print(*E)
print(*F)
print(*G)







