import math 
n, r = list(map(int, input().split()))
R = r * math.sin( math.pi/n )  / ( 1 - math.sin( math.pi/n ))
print("%.9f"%(R))

