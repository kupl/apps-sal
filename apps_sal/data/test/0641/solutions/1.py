p=input().split()
if p[2]=='week':
    x=int(p[0])
    if x==5 or x==6:
        print(53)
    else:
        print(52)
else:
    x=int(p[0])
    if x<=29:
        print(12)
    elif x==30:
        print(11)
    else:
        print(7)

