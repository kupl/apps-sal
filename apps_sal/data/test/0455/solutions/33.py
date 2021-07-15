#!/usr/bin/env python3

def main():
    N = int(input())
    XY_list = []
    for i in range(N):
        XY_list.append(list(map(int, input().split())))

    rot_list = list([[xy[0] + xy[1], -xy[0] + xy[1]] for xy in XY_list])

    f = True
    p = rot_list[0][0] % 2
    for i in range(1, N):
        if rot_list[i][0] % 2 != p:
            f = False
            break

    if not f:
        print((-1))
    else:
        offset = 2 ** 31 - p
        m = 32 - p
        d = []
        if p == 0:
            d.append(1)
        for k in range(31):
            d.append(2 ** k)
        w = []
        for i in range(N):
            uv = rot_list[i]
            u, v = uv[0] + offset, uv[1] + offset
            s = ''
            if p == 0:
                s = 'D'
            for k in range(31):
                u //= 2
                v //= 2
                u1, v1 = u % 2, v % 2
                if u1 == 0 and v1 == 0:
                    s += 'D'
                elif u1 == 0 and v1 == 1:
                    s += 'L'
                elif u1 == 1 and v1 == 0:
                    s += 'R'
                elif u1 == 1 and v1 == 1:
                    s += 'U'
            w.append(s)

        print(m)
        s = ''
        for dv in d:
            s += ' ' + str(dv)
        print((s[1:]))
        for i in range(N):
            print((w[i]))


def __starting_point():
    main()


__starting_point()
