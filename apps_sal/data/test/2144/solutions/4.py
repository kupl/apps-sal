from math import gcd
t = int(input())


for _ in range(t):
    a, m = map(int, input().split())

    b = m//gcd(a, m)

    p = set()
    pow = {}

    i = 2
    while (i*i<=b):
        while (b%i==0):
            if i not in p:
                p.add(i)
                pow[i] = 0
            pow[i]+=1
            b//=i
        i+=1
    if (b>1):
        p.add(b)
        pow[b] = 1

    ans = 1
    for prost in p:
        ans*=prost**(pow[prost]-1)*(prost-1)
    print(ans)
