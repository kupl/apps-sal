import math
import re
def ria():
    return [int(i) for i in input().split()]
a,b=ria()
c=b-a
if c>=20:
    print(0)
else:
    kek=1
    
    for i in range(a+1,b+1):
        kek*=i

    print(kek%10)

