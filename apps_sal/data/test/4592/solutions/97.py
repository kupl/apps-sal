import math

def is_prime(n):
    if(n == 1):
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i == 0):
            return False
        
    return True

sosu = []
for i in range(1, 1001):
    if(is_prime(i)):
        sosu.append(i)    

N = int(input())
mod = 10**9+7
x = math.factorial(N)
a = 1

for i in range(len(sosu)):
    cnt = 0
    if(sosu[i] > x):
        break
    while (x%sosu[i]==0):
        x = x//sosu[i]
        cnt += 1
    if(cnt):
        a *= (cnt+1)
        a %= mod

print(a)
