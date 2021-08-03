def solve():
    K = int(input())

    e = [["++", "**"], ["+*", "*+"]]
    vs = ["+"]
    for i in range(K):
        nv = []
        for j in range(2):
            for v in vs:
                x = []
                for c in v:
                    x.append(e[j][0] if c == '+' else e[j][1])
                nv.append(''.join(x))
        vs = nv

    for v in vs:
        print(v)


def __starting_point():
    solve()


__starting_point()
