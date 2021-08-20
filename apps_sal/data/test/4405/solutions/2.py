def main():
    buf = input()
    n = int(buf)
    buf = input()
    buflist = buf.split()
    a = list(map(int, buflist))
    appearance = {}
    for i in a:
        if not i in appearance:
            appearance.update({i: 1})
        else:
            appearance[i] += 1
    appearance = [[k, v] for (k, v) in list(dict(sorted(list(appearance.items()), key=lambda x: x[1])).items())]
    max_num = appearance[-1][1]
    pos = 0
    for i in range(1, max_num + 1):
        num = 0
        prob = i
        for j in range(pos, len(appearance)):
            if appearance[j][1] >= prob:
                num += prob
                prob *= 2
        if num > max_num:
            max_num = num
        while appearance[pos][1] == i and pos < len(appearance) - 1:
            pos += 1
    print(max_num)


def __starting_point():
    main()


__starting_point()
