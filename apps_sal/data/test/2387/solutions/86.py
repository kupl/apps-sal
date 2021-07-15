def main():
    n = int(input())
    up = []
    down = []
    for _ in range(n):
        height = 0
        m = 0
        for si in input():
            if si == "(":
                height += 1
            else:
                height -= 1
                m = min(m, height)
        if height >= 0:
            up.append([m, height])
        else:
            down.append([m-height, -height])
    up.sort(reverse=True)
    down.sort(reverse=True)
    if sum([i for _, i in up]) - sum([i for _, i in down]) != 0:
        print("No")
        return
    h = 0
    for mi, hi in up:
        if h+mi < 0:
            print("No")
            return
        h += hi
    h = 0
    for mi, hi in down:
        if h+mi < 0:
            print("No")
            return
        h += hi
    print("Yes")
    return
            

def __starting_point():
    main()
__starting_point()
