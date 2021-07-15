a, b, c,d = (int(x) for x in input().split())

kyori1 = a - c
kyori2 = a - b
kyori3 = b - c

if abs(kyori1) <= d or (abs(kyori2) <= d and abs(kyori3) <= d) :
    print('Yes')
else :
    print('No')
