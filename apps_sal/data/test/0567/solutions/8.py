
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    mm = 0
    for aa in a:
        m = min(aa - 1, 1000000 - aa)
        mm = max(mm, m)
    print(mm)


def __starting_point():
    main()


__starting_point()
