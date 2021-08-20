import itertools


def main():
    g = list()
    for i in range(5):
        g.append(list(map(int, input().split())))
    print(max([g[l[0]][l[1]] + g[l[1]][l[0]] + 2 * g[l[2]][l[3]] + 2 * g[l[3]][l[2]] + g[l[1]][l[2]] + g[l[2]][l[1]] + 2 * g[l[3]][l[4]] + 2 * g[l[4]][l[3]] for l in itertools.permutations(list(range(5)))]))


def __starting_point():
    main()


__starting_point()
