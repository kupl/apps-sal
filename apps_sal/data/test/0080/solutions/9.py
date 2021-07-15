import math

def get_div(n):
    a = []
    for i in range(1,int(n**.5)+1):
        if n % i == 0:
            a.append([i,n//i])
    return a

tmp = [int(i) for i in input().split()]
l,r,x,y = tmp[0],tmp[1],tmp[2],tmp[3]
if y % x != 0:
    print(0)
else:
    c = 0
    a = get_div(y//x)
    for p in a:
        pl = min(p)
        pr = max(p)
        if math.gcd(pl,pr) == 1:#(1 in p) or (pr % pl != 0):
            if l <= x * pl and x * pr <= r:
                c += 1
                if p[0] != p[1]:
                    c += 1
    print(c)

