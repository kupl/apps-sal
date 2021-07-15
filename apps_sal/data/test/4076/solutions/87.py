import math
 
A, B, H, M = map(int, input().split())
 
angle_A = 6*M
angle_B = 30*(H+M/60)
angle_C = abs(angle_A-angle_B)
 
rad_C = math.radians(angle_C)
 
C = math.sqrt(A**2+B**2-2*A*B*math.cos(rad_C))
 
print(C)
