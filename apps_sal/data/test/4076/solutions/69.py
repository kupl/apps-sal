import math

a, b, h, m = map(int, input().split())

alpha = 2*math.pi * h/12 + (math.pi/6) *m/60
beta = 2*math.pi * m/60

ans = (a*a + b*b - 2*a*b*math.cos(alpha - beta)) **0.5
print(ans)
