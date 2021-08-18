

def main():
    dest, battmax, accumax = list(map(int, input().split()))
    batt = battmax
    accum = accumax

    light = list([bool(int(x)) for x in input().split()])
    path = 0
    for i in range(len(light)):
        if not batt and not accum:
            break
        if accum == accumax:
            accum -= 1
            path += 1
        elif batt > 0 and light[i]:
            batt -= 1
            accum += 1
            path += 1
        elif accum > 0:
            accum -= 1
            path += 1
        else:
            batt -= 1
            path += 1
    print(path)


def __starting_point():
    main()


__starting_point()
