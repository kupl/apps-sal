from decimal import Decimal
import math
a,b=map(str,input().split())

c=math.floor(Decimal(a)*Decimal(b))

print(c)
