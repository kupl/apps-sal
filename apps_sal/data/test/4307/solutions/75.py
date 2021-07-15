import math

def primefac(n):
    s = []
    x = int(math.sqrt(n))+1
    for i in range(2,x+1):
        if n%i == 0:
            cnt= 0
            while n%i == 0:
                n //=i
                cnt += 1
            s.append([i,cnt])
    if n != 1:
        s.append([n,1])
    return(s)
  
n = int(input())
ans = 0
for i in range(1,n+1):
    x = 1
    s = primefac(i)
    for t in s:
        x *= t[1]+1
    if x == 8 and i%2 == 1:
        ans += 1
print(ans)
    

