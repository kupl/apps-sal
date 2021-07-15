a,b,c,d=map(int,input().split())
dcou=b//d-(a-1)//d
ccou=b//c-(a-1)//c
from math import gcd
dc=d*c//gcd(d,c)
dccou=b//dc-(a-1)//dc
ans=b-a-dcou-ccou+dccou+1
print(int(ans))
