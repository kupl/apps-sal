from math import ceil


n,a,b,c,d,e = [int(input()) for i in range(6)]
print((ceil(n/min(a,b,c,d,e))+4))

