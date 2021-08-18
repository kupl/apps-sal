def VI(): return list(map(int, input().split()))
def Y(): print("YES")


def run(w, m):
    if w <= 3:
        Y()
        return
    mm = m
    for i in range(100):
        if m % w == 0:
            m //= w
        elif m % w == 1:
            m = (m - 1) // w
        elif m % w == w - 1:
            m = (m + 1) // w
        else:
            break
        if m == 0:
            Y()
            return

    print("NO")


def main(info=0):
    w, m = VI()
    run(w, m)


def __starting_point():
    main()


__starting_point()
