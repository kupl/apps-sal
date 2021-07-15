from decimal import Decimal,getcontext
from math import ceil
getcontext().prec = 1000
N = int(input())
 
takahashi,aoki = 1,1
 
for _ in range(N):
    a,b = map(int,input().split())
    c = max(ceil(Decimal(str(takahashi))/Decimal(a)),ceil(Decimal(str(aoki))/Decimal(b)))
    takahashi = c*a
    aoki = c*b
 
print(takahashi+aoki)
