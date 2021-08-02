
def main(stdin):
    n, m = next(stdin).split()
    n, m = int(n), int(m)
    a_i = next(stdin).split()
    checked = {}
    diff = {}

    checked[int(a_i[-1])] = 1
    diff[n - 1] = 1
    for i in range(n - 2, -1, -1):
        diff[i] = diff[i + 1]
        if int(a_i[i]) not in checked:
            diff[i] += 1
            checked[int(a_i[i])] = 1

    for l in stdin:
        print(diff[int(l) - 1])


def __starting_point():
    import sys
    main(sys.stdin)


__starting_point()
