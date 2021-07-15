def divisor(n):
    res = []
    
    i = 1
    while i*i <= n:
        if not n % i:
            res.append(i)
            if (i*i != n): res.append(n//i)     
        
        i += 1
        
    return res

N = int(input())
ans = 0

for d in divisor(N):
    if d == 1: continue
    n = N
    
    while not n % d:
        n //= d
        
    if n%d == 1: ans += 1
    
print(ans + len(divisor(N-1))-1)
