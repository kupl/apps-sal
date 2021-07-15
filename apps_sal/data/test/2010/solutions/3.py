def main():
    n, m = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    delta, res = 0, []
    for _ in range(m):
        l = list(map(int, input().split()))
        if l[0] == 1:
            aa[l[1] - 1] = (l[2], delta)
        elif l[0] == 2:
            delta += l[1]
        else:
            x = aa[l[1] - 1]
            res.append(str((x[0] - x[1] if type(x) is tuple else x) + delta))
    print('\n'.join(res))


def __starting_point():
    main()

__starting_point()
