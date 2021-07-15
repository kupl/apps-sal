import math
A, B, H, M = map(int,input().split())
h = 30*H + (0.5)*M
m = 6*M
C = abs(h-m)
X = math.sqrt(A**2 + B**2 -(2*A*B*(math.cos(math.radians(C)))))
print(X)
