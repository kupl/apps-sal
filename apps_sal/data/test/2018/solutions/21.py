from sys import stdin
def gcd(a,b):
    while b!=0:
        t=int(a)
        a=int(b)
        b=t%a
    return int(a)
def lcm(a, b):
    return int((a*b)/gcd(a, b))
n,m,q=list(map(int,stdin.readline().strip().split()))
b=lcm(n,m)//n
a=lcm(n,m)//m
for i in range(q):
    x,y,x1,y1=list(map(int,stdin.readline().strip().split()))
    if (x==2):
        w=y//b
        if (y%b!=0):
            w+=1
    else:
        w=y//a
        if (y%a!=0):
            w+=1

    if (x1==2):
        w1=y1//b
        if (y1%b!=0):
            w1+=1
    else:
        w1=y1//a
        if (y1%a!=0):
            w1+=1
    if w==w1:
        print("YES")
    else:
        print("NO")

