n,k=map(int,input().split())
a=10**k
def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)
print(lcm(n,a))
