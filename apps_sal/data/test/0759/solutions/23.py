import math
hh,mm = [int(x) for x in input().split()]
h,d,c,n = [int(x) for x in input().split()]
if hh>=20:
    print(0.8*c*math.ceil(h/n))
else:
    print(min(0.8*c*math.ceil(((((20-hh)*60-mm)*d)+h)/n),c*math.ceil(h/n)))
