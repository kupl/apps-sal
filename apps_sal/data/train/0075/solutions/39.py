import math
def solve(n):
    alpha = 2*math.pi/(4*n)
    ratio = math.sin(alpha)
    half = 0.5/ratio
    ag = 180/(4*n)
    ag = ag*2*math.pi/360
    return half*2*math.cos(ag)
t = int(input())
for _ in range(t):
    s = int(input())
    print(solve(s))
    

