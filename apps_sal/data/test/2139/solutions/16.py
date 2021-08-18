
def main():
    s = input()
    n = len(s)
    pos = [-1]
    p = 0
    while True:
        p = s.find("bear", p)
        if p == -1:
            break
        pos.append(p)
        p += 4
    ret = 0
    m = len(pos)
    for i in range(1, m):
        ret += (pos[i] - pos[i - 1]) * (n - pos[i] - 3)
    print(ret)


def __starting_point():
    main()


__starting_point()
