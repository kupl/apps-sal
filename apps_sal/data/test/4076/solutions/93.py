import math
A, B, H, M=list(map(int, input().split()))

wa=math.pi*2/60/12
wb=math.pi*2/60
theta=(wb-wa)*(H*60+M)%(2*math.pi)

print(((A**2+B**2-2*A*B*math.cos(theta))**0.5))

