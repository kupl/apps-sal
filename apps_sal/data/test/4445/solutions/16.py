def GI():
    return int(input())


def GIS():
    return list(map(int, input().split()))


def LGIS():
    return list(GIS())


def main():
    GI()
    xs = GIS()
    ps = [[], []]
    for x in xs:
        ps[x % 2].append(x)
    ps.sort(key=len)
    lendiff = len(ps[1]) - len(ps[0])
    if lendiff > 1:
        large = ps[1]
        large.sort()
        print(sum(large[:lendiff - 1]))
    else:
        print(0)


main()
