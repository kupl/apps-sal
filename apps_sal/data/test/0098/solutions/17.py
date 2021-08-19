def main():
    a, b = list(map(int, input().split()))
    obj = [None, None]
    obj[0] = list(map(int, input().split()))
    obj[1] = list(map(int, input().split()))

    # portrait
    def vlezet(a, b, i, j, sx, sy):
        return (i + sx <= a) and (j + sy <= b)

    if vlezet(a, b, 0, 0, *obj[0]):
        x = obj[0][0]
        y = obj[0][1]
        if vlezet(a, b, x, 0, *obj[1]) or vlezet(a, b, x, 0, obj[1][1], obj[1][0]):
            print('YES')
            return 0
        elif vlezet(a, b, 0, y, *obj[1]) or vlezet(a, b, 0, y, obj[1][1], obj[1][0]):
            print('YES')
            return 0

    obj[0][1], obj[0][0] = obj[0][0], obj[0][1]
    if vlezet(a, b, 0, 0, *obj[0]):
        x = obj[0][0]
        y = obj[0][1]
        if vlezet(a, b, x, 0, *obj[1]) or vlezet(a, b, x, 0, obj[1][1], obj[1][0]):
            print('YES')
            return 0
        elif vlezet(a, b, 0, y, *obj[1]) or vlezet(a, b, 0, y, obj[1][1], obj[1][0]):
            print('YES')
            return 0
    print('NO')
    return 0


main()
