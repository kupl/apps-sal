import math
t = int(input())
for _ in range(t):
    n = int(input())
    print("{:.10f}".format(math.cos(math.pi/(4*n))/math.sin(math.pi/(2*n))))
    

