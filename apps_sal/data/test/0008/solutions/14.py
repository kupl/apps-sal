def main():
    buf = input()
    buflist = buf.split()
    hand = buflist
    t = []
    for i in range(3):
        t.append([])
        for j in range(9):
            t[i].append(0)
    for x in hand:
        idx = 0
        if x[1] == 'm':
            idx = 0
        elif x[1] == 'p':
            idx = 1
        elif x[1] == 's':
            idx = 2
        t[idx][int(x[0]) - 1] += 1
    max_cons = 0
    max_mult = 0
    for i in range(3):
        cons = [0, 0, 0]
        for j in range(9):
            cons[0] = cons[1]
            cons[1] = cons[2]
            if t[i][j] > 0:
                cons[2] = 1
            else:
                cons[2] = 0
            max_cons = max(sum(cons), max_cons)
            max_mult = max(max_mult, t[i][j])
    print(3 - max(max_cons, max_mult))


def __starting_point():
    main()


__starting_point()
