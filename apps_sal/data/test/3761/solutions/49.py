def main():

    s = input()
    x, y = map(int, input().split())
    n = len(s)

    x1, y1 = 0, 0
    i = 0
    while i < n and s[i] == "F":
        x1 += 1
        i += 1

    count = 0
    UD = []
    LR = []
    while i < n:
        if s[i] == "T":
            count += 1
            i += 1
        else:
            d = 0
            while i < n and s[i] == "F":
                d += 1
                i += 1
            if count % 2 == 1:
                UD.append(d)
            else:
                LR.append(d)

    s1 = set([x1])
    for v in LR:
        temp = set()
        for u in s1:
            temp.add(u + v)
            temp.add(u - v)
        s1 = temp
    if x not in s1:
        return "No"
    s2 = set([0])
    for v in UD:
        temp = set()
        for u in s2:
            temp.add(u + v)
            temp.add(u - v)
        s2 = temp
    if y not in s2:
        return "No"

    return "Yes"


def __starting_point():
    print(main())


__starting_point()
