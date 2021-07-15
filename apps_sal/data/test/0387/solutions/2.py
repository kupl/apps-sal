import math

a, b = [int(x) for x in input().split()]
cnt = 0
ab = a + b
k = 2
while k <= ab:
    t = ab // k
    aPeriod = a // t
    bPeriod = b // t
    aLeft = (a + t) // (t + 1)
    bLeft = (b + t) // (t + 1)
    arem = a - t * aPeriod
    brem = b - t * bPeriod
    if aPeriod >= arem and bPeriod >= brem:
    	validK = aPeriod + bPeriod - aLeft - bLeft + 1
    	if (t + 1) * (aLeft + bLeft) == ab:
    		validK -= 1
    	if validK > 0:
    		cnt += validK
    k = ab // t + 1
print(cnt)
