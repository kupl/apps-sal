from itertools import accumulate


def main():
    (n, w) = [int(_) for _ in input().split()]
    a = [int(_) for _ in input().split()]
    c = list(accumulate(a))
    ans = min(w, w - max(c)) - max(-min(c), 0) + 1
    if ans <= 0:
        print(0)
    else:
        print(ans)


def __starting_point():
    main()


__starting_point()
