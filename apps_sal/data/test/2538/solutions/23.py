for q in range(int(input())):
    x, y, z = list(map(int, input().split()))
    if x <= y:
        z -= y-x+1
        if z < 0:
            print(0)
        else:
            print(z//2+1)
    elif z < x-y:
        print(z+1)
    else:
        z -= x-y+1
        print(x-y+z//2+1)

