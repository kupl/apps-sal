def main():
    n = int(input())
    p = [int(pn) for pn in input().split()]
    ans = 0
    is_changed = False
    for i in range(n):
        if is_changed:
            is_changed = False
        elif p[i] == i + 1:
            is_changed = True
            ans += 1
    print(ans)


def __starting_point():
    main()

__starting_point()
