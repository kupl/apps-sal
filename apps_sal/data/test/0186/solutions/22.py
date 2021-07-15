import sys




##Wrong answer... not finished
def main():
    n, m = [int(f) for f in sys.stdin.readline().split()]

    h = max(2 * n, 3 * m)

    n_common = h // 6

    n3 = h // 3 - n_common
    n2 = h // 2 - n_common


    if (n3 + n2 + n_common) >= (m + n):
        res = h
    else:
        while n3 + n2 + n_common < m + n:
            h += 1

            if h % 2 != 0 and h % 3 != 0:
                continue

            n_common = h // 6
            n3 = h // 3 - n_common
            n2 = h // 2 - n_common
        res = h

    print(res)




def __starting_point():
    main()

__starting_point()
