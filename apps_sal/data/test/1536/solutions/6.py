def solve(n, p):
    p = sorted(p, key=lambda x: (x[0], x[1], x[2]))
    # print('solve', p)
    p.append([10**20, 10**20, 10**20, 10**20])
    # eliminate matching x coord ones:
    c = 1
    pn = []
    for i in range(1, len(p)):
        if p[i][0] == p[i - 1][0]:
            c += 1
        else:
            if c >= 2:
                s = solve_2d(p[i - c:i])
                if s:
                    pn.append(s)
            else:
                pn.append(p[i - 1])
            c = 1
    # print(pn)
    for i in range(0, len(pn) - 1, 2):
        print(pn[i][3], pn[i + 1][3])


def solve_2d(p1):
    # print('solve_2d', p1)
    p1.append([10**20, 10**20, 10**20, 10**20])
    c = 1
    p1n = []
    i = 1
    while i < len(p1):
        if p1[i][1] == p1[i - 1][1]:
            print(p1[i][3], p1[i - 1][3])
            i += 2
        else:
            p1n.append(p1[i - 1])
            i += 1
    for i in range(0, len(p1n) - 1, 2):
        print(p1n[i][3], p1n[i + 1][3])
    if len(p1n) % 2 == 1:
        return p1n[-1]
    else:
        return 0


def main():
    n = int(input())
    p = []
    for i in range(n):
        pt = [int(i) for i in input().split()]
        p.append(pt + [i + 1])
    solve(n, p)


main()
