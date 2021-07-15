import math
def factors(k):
    L = []
    for i in range(2,int(math.sqrt(k))+1):
        if k % i == 0:
            if i == k//i:
                L.append(i)
            else:
                L.append(i)
                L.append(k//i)
    L.append(k)
    return L
    

def prime(p):
    for i in range(2,int(math.sqrt(p))+1):
        if p % i == 0:
            return 0
    return 1


n = int(input())
if n % 2 == 0:
    print(n//2)
else:
    a = factors(n)
    for i in a:
        if prime(i):
            print(((n-i)//2)+1)
            break
