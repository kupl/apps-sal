t=int(input())
for i in range (t):
    ang = int(input())
    if ang==179:
        print (360)
        continue
    for n in range (3,181):
        if ang*n%180==0 and ang*n//180<n-1:
            print (n)
            break
