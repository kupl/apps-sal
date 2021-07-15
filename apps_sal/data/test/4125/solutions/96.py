import  math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

N,X=list(map(int,input().split()))
x=sorted(list((list(map(int,input().split())))))
y=[abs(i-X) for i in x ]
print((gcd_list(y)))

