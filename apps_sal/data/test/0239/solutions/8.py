import math

def __starting_point():
    (x,y) = (int(a) for a in input().split(' '))
    ans = []
    if x == 0:
##        print('Enters 1')
        ans.append((0,1))
        ans.append((0,y))
        ans.append((0,0))
        ans.append((0,y-1))
    elif y == 0:
##        print('Enters 2')
        ans.append((1,0))
        ans.append((x,0))
        ans.append((0,0))
        ans.append((x-1,0))
    else:
        if x > y:
            if (y < 2) or (math.sqrt(x**2 + y**2) + x > 2*math.sqrt(x**2 + (y-1)**2)):
##                print('Enters 3')
                ans.append((0,0))
                ans.append((x,y))
                ans.append((0,y))
                ans.append((x,0))
            else:
##                print('Enters 4')
                ans.append((0,1))
                ans.append((x,y))
                ans.append((0,0))
                ans.append((x,y-1))
        else:
            if (x < 2) or (math.sqrt(x**2 + y**2) + y > math.sqrt(y**2 + (x-1)**2) + math.sqrt(y**2 + (x-1)**2)):
##                print('Enters 5')
                ans.append((0,0))
                ans.append((x,y))
                ans.append((x,0))
                ans.append((0,y))
            else:
##                print('Enters 6')
                ans.append((1,0))
                ans.append((x,y))
                ans.append((0,0))
                ans.append((x-1,y))
    for a in ans:
        print(str(a[0])+' '+str(a[1]))
        

__starting_point()
