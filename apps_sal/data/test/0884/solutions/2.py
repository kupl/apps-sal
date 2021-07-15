import math
f = 998244353
            
def matchings(a,b):
    m = max(a,b)
    n = min(a,b)
    
    t = 1
    p = 1
    for i in range(0,n):
        p *= (n-i)*(m-i)
        p //= i+1
        t += p
    t = t % f
    return(t)

inputs = [int(x) for x in input().split(" ")]
k = matchings(inputs[0],inputs[1])*matchings(inputs[0],inputs[2])*matchings(inputs[2],inputs[1]) % f
print(k)
