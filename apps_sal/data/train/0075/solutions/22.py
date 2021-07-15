import math

for _ in range(int(input())):
    n=int(input())
    s=2*n
    #side = (((1/2*(math.sin(math.pi/(2*s))))**2)-1)**.5
    side = 1/(2*(math.sin(math.pi/(2*s))))
    print(side)
