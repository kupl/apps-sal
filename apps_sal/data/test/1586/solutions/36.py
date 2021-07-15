N=int(input());a=10;b=0
if N&1==0:
    while a<=N:b+=N//a;a*=5
print(b)
