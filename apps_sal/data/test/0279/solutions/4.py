a, b = list(map(int, input().split(' ')))
t, d = list(map(int, input().split(' ')))
if d == 0:
    print(a*t)
else:
    dist=0
    t-=1
    dist+=a
    if t == 0:
        print(dist)
        quit()

    
    while (a-b)+d<=(t-1)*d:
        a += d
        dist += a
        t -= 1
    if t == 0:
        print(dist)
        quit()
        
    extra = -1*(a-b-d*(t-1))
    a += extra
    dist += a
    t -= 1


    while t > 0:
        a -= d
        t -= 1
        dist += a
    print(dist)

