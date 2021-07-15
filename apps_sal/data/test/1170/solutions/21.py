import math

t = int(input())

for _ in range(t):
    x = int(input())
    
    found = False
    for n in range(int(math.sqrt(x))+1, int(10**4.6)):
        m = n/math.sqrt(n**2-x)
        m1 = math.ceil(m)
        m2 = math.floor(m)
        
        for m in [m1, m2]:
            if n**2-(n//m)**2==x:
                print(n, m)
                found = True
                break
        if found:
            break
    if not found:
        print(-1)            

