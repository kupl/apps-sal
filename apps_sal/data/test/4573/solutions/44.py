n = int(input())
xlist = list(map(int, input().split()))
tmpx = sorted(xlist)
(med1, med2) = (tmpx[n // 2 - 1], tmpx[n // 2])
for x in xlist:
    if x <= med1:
        print(med2)
    else:
        print(med1)
