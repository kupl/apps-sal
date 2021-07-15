import math
A,B,H,M = map(int,input().split())
a = (H*60+M)*0.5
b = M*6
angle = math.radians(min(abs(b-a),360-abs(b-a)))
cos = math.cos(angle)
ans = A**2 + B**2 - 2*A*B*cos
print(ans**0.5)
