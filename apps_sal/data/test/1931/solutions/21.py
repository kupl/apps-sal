import math
t = int(input())
import math
delay = []
for _ in range(t):
    n = int(input())
    k = 0
    while(n > 0):
        x = math.floor(((24*n+1)**(0.5) - 1)/6)
        if x <= 0:
            break
        n -= x*(3*x+1)/2
        k+=1 
    print(k)
