for q in range(int(input())):
    x, y, z = list(map(int, input().split()))
    h, c = list(map(int, input().split()))
    if h < c:
        y, z, h, c = z, y, c, h
    if x <= y*2:
        print(x//2*h)
    else:
        print(y*h+min((x-2*y)//2, z)*c)

