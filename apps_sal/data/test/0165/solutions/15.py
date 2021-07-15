def __starting_point():
    arr = [int(ch) for ch in input().split(' ')]

    a = arr[0]
    b = arr[1]
    c = arr[2]

    if a == b and  a == c:
        print('0')
        return

    maximum = max(a, b, c)
    res = True
    for i in arr:
        if i != maximum or i != (maximum - 1):
            res = False
    if res:
        print('0')
        return

    adding = 0
    for i in arr:
        if i == maximum:
            continue
        else:
            adding += maximum - i - 1

    print(adding)
__starting_point()
