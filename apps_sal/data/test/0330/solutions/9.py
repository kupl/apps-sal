p,y = list(map(int,input().split()))
import math
def is_prime(n,p):
    if n % 2 == 0 and n > 2: 
        return False
    if p == 2: return True
    for i in range(3, min(p,int(math.sqrt(n)))+1, 2):
        if n % i == 0:
            return False
    return True
for x in range(y,p,-1):
    if is_prime(x,p):
        print(x)
        break
else:
    print(-1)


