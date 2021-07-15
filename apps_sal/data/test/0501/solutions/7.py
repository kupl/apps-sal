l, r = input().split()

l = int(l)
r = int(r)

MOD = 10**9+7

def f(v) :
    nonlocal MOD
    ret = 0
    r = 0
    
    p1, p2 = 0, 0

    while (v>>r) > 0:
        if r&1 == 0:
            p1 += min(v+1, 1<<r+1)-(1<<r)
        else :
            p2 += min(v+1, 1<<r+1)-(1<<r)
        r += 1
    
    return (p1*p1+p2*(p2+1))%MOD
print((f(r)-f(l-1)+MOD)%MOD)
