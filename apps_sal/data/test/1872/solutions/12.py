import math
PI = math.acos(-1)

n, R = list(map(int, input().split()))
ag = 2*PI / n
L = 2 * math.sin(ag/2) * R

SP = n * L / 2 * R * math.cos(ag/2) 

ang = (PI - ag - ag / 2) / 2
S = L**2 / 4 * math.tan(ang)
SS = SP - S * n
print("%.10f" % SS)
    

