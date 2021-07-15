def main():
    n,l,x,y = list(map(int,input().split()))
    arr = set(map(int,input().split()))
    first = False
    second = False
    for i in arr:
        if i+x in arr:
            first = True
        if i+y in arr:
            second = True

    if first and not second:
        print(1)
        print(y)
        return
    if second and not first:
        print(1)
        print(x)
        return
    if first and second:
        print(0)
        return

    found = False
    for i in arr:
        if i+x-y in arr and i+x <= l:
            found = True
            coord = i+x
            break

        if i+y-x in arr and i+y <= l:
            found = True
            coord = i+y
            break

        if i+x+y in arr and i+min(x,y) <= l:
            found = True
            coord = i+min(x,y)

        if i-x-y in arr and i-max(x,y) >= 0:
            found = True
            coord = i-max(x,y)

        if i-x+y in arr and i-x >= 0:
            found = True
            coord = i-x
            break

        if i-y+x in arr and i-y >= 0:
            found = True
            coord = i-y
            break

        if found:
            break

    if found:
        print(1)
        print(coord)
        return

    print(2)
    print(x,y)


main()

