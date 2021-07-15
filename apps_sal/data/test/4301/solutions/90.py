n = int(input())

a = [0] * n

fm, fi = 0, 0
sm, si = 0, 0  
for i in range(n):
    a[i] = int(input())
    if a[i] > fm:
        sm, si = fm, fi
        fm, fi = a[i], i
    elif a[i] > sm:
        sm, si = a[i], i
        
for i in range(n):
    if i != fi:
        print(fm)
    else:
        print(sm)        
