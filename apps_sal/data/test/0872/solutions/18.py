def solution():
    n = input()
    ar = list(map(int, input().split()))
    o, e = False, False
    for i in ar:
        if i % 2 == 0:
            o = True
        else:
            e = True
    if o and e:
        ar = sorted(ar)
    for a in ar:
        print(a, end=' ')


def __starting_point():
    solution()


__starting_point()
