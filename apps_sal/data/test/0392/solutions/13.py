from math import sqrt

f = {}
def factor(n):
    if n in f:
        return f[n]
    
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)

    factors = sorted(factors, reverse = True)
    f[n] = factors
            
    return factors
  
n = int(input())

for i in factor(n):
    is_success = True
    for j in factor(i):
        if j > 1:
            s = sqrt(j)
            if s == int(s):
                is_success = False
                break
    if is_success:
        print(i)
        return

