import sys
import math


def main():
    n,m = map(int,sys.stdin.readline().split())
    x = list(map(int,sys.stdin.readline().split()))

    c = []
    nc = []
    d = {}
    for i in range(n):
        xi = x[i]
        if xi in d:
            continue
        d[xi] = True
        if xi%2 == 0:
            c.append((xi,i))
        else:
            nc.append((xi,i))

    a, b = -1,0

    if len(nc) > len(c):
        c,nc = nc,c
        a,b = b,a

    c = sorted(c, key=lambda x: -x[0])
    d = {}
    r = [0]*n
    for i in range(len(nc)):
        xi,j = nc[i]
        r[j] = xi
        d[xi]= True
        
    for i in range(min(n//2,len(c))):
        xi,j = c[i]
        r[j] = xi
        d[xi]= True
    
    j=0    
    ans=0
    for i in range(len(c),n//2):
        b+=2
        while b in d:
            b+=2
        while r[j]!=0:
            j+=1 
        r[j] = b
        ans+=1
    for i in range(len(nc),n//2):
        a+=2
        while a in d:
            a+=2
        while r[j]!=0:
            j+=1 
        r[j] = a
        ans+=1

    if a>m or b>m:
        print(-1)
        return 
    
    print(ans)
    
    print(' '.join(map(str,r)))


main()
