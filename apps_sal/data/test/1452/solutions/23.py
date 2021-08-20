def main():
    from array import array
    import sys
    (h, w) = map(int, sys.stdin.readline().split())
    grid = tuple((tuple((array('b', (0,)) for _ in range(w))) for _ in range(h)))
    ans = h * w
    arr1 = array('b', (1,))
    for _ in range(2):
        for (row, r) in zip(grid, map(int, sys.stdin.readline().split())):
            arr1r = arr1 * r
            arr1r.append(-1)
            for (elem, value) in zip(row, array('b', arr1r)):
                if not elem[0]:
                    elem[0] = value
                    ans -= 1
                elif elem[0] != value:
                    return print('0')
        grid = zip(*grid)
    return print(pow(2, ans, 1000000007))


main()
