def findNumbers(s):
    t = [0]*25
    i = (s//50)%475
    for k in range(25):
        i = (i * 96 + 42) % 475
        t[k] = i+26
    return t

p, x, y = list(map(int, input().split() ))

k = 0

if x >= y:
    xt = x

    while (p not in findNumbers(xt) and xt >= y ):
        xt -= 50
    if p in findNumbers(xt) and xt >= y:
        print(0)
    else:
        xt = x
        while (p not in findNumbers(xt)):
            xt += 50
            k+=0.5
##            print(str(k) + " " + str(xt) )
        
        print( int(k+0.5))
else:
    k = (y-x) // 100
    xt = ((y-x) // 100) * 100 + x
    if xt<y:
        xt+=100
        k+=1
##    print(xt)
    while (p not in findNumbers(xt) and xt >= y ):
        xt -= 50
    if p in findNumbers(xt) and xt >= y:
        print(k)
    else:
        xt = x
        while (p not in findNumbers(xt)):
            xt += 50
            k+=0.5
##            print(str(k) + " " + str(xt) )
        
        print( int(k+0.5))
    

