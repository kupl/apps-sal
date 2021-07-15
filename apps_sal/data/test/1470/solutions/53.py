x = int(input())

if x <= 6:
    print(1)
elif x <= 11:
    print(2)
else:
    d = x//11
    m = x%11

    if m == 0:
        print(d*2)
    elif m <= 6:
        print(d*2+1)
    else:
        print(d*2+2)
