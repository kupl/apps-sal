a, b, f, k = [int(i) for i in input().split()]

##tank = b
##journeys = 0
##refuels = 0
##current = 0
##while(journeys != k):
##    print("current = %d, tank = %d, refuels = %d, journeys = %d" % (current, tank, refuels, journeys))
##    if (tank // a >= k):
##        print(refuels)
##        return
        
##    if current == 0:
##        if tank >= a + (a-f):
##            tank -= a
##        elif tank >= f and b >= a-f:
##            refuels += 1
##            tank = b-(a-f)
##        else:
##            break
##        
##        current = a
##        
##    elif current == a:
##        if tank >= a + f:
##            tank -= a
##        elif tank >= a-f and b >= f:
##            refuels += 1
##            tank = b-f
##        else:
##            break
##        
##        current = 0
##
##    journeys += 1

if b < f:
    print(-1)
    return

journeys = 0
previous = 0
refuels1 = 0
tank = b-f
while(journeys != k): ## necessary? while(True) ?
    if previous == 0:
        if tank >= a-f + a*(k-journeys-1):
            print(refuels1)
            return
        if b >= a-f + a*(k-journeys-1):
            print(refuels1+1)
            return
        if tank >= 2*(a-f):
            tank -= 2*(a-f)
        elif b >= 2*(a-f):
            refuels1 += 1
            tank = b - 2*(a-f)
        else:
            print(-1)
            return
        
        journeys += 1
        previous = a
        
    if previous == a:
        if tank >= f + a*(k-journeys-1):
            print(refuels1)
            return
        if b >= f + a*(k-journeys-1):
            print(refuels1+1)
            return
        if tank >= 2*f:
            tank -= 2*f
        elif b >= 2*f:
            refuels1 += 1
            tank = b-2*f
        else:
            print(-1)
            return
        
        journeys += 1
        previous = 0

if journeys == k:
    print(refuels1)
else:
    print(-1)

##journeys = 0
##previous = 0
##refuels2 = 1
##tank = b
##cant2 = False
##while(journeys != k):
##    if previous == 0:
##        if tank >= a-f + a*(k-journeys-1):
##            break
##        if tank >= 2*(a-f):
##            tank -= 2*(a-f)
##        elif b >= 2*(a-f):
##            refuels2 += 1
##            tank = b - 2*(a-f)
##        else:
##            cant2 = True
##            break
##        
##        journeys += 1
##        previous = a
##        
##    if previous == a:
##        if tank >= f + a*(k-journeys-1):
##            break
##        if tank >= 2*f:
##            tank -= 2*f
##        elif b >= 2*f:
##            refuels2 += 1
##            tank = b-2*f
##        else:
##            cant2 = True
##            break
##        
##        journeys += 1
##        previous = 0
##
##if cant1 and not cant2:
##    print(refuels2)
##elif not cant1 and cant2:
##    print(refuels1)
##elif cant1 and cant2:
##    print(-1)
##else:
##    print(min(refuels1, refuels2))


