def inint():
    return int(input())


def inlist():
    return list(map(int, input().split()))


def main():
    (n, t) = inlist()
    a = inlist()
    sol = 0
    while True:
        ss = 0
        amt = 0
        for i in a:
            if i <= t:
                sol += 1
                ss += i
                t -= i
                amt += 1
        if amt == 0:
            break
        sol += t // ss * amt
        t = t % ss
    print(sol)


def __starting_point():
    main()


__starting_point()
