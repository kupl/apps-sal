import math
n,a=list([int(m) for m in input().split(' ')])
if(a%2):
    print(math.ceil(a/2))
    return
else:
    print(n//2-a//2+1)

