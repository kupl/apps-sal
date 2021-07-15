x = int(input())

if x <= 11:
    if x <= 6:
        print(1)
    else:
        print(2)
        
else:
    rot = x//11
    mod = x%11
    if mod > 6:
        print(2*rot + 2)
        return
    if mod > 0:
        print(2*rot + 1)
        return
    print(2*rot)
