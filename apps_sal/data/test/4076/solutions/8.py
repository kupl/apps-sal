import math

A, B, H, M = list(map(int,input().split()))

q = abs((H + M/60)/12-M/60)*360

print((math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(q)))))

