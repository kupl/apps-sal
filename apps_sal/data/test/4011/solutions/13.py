import sys


def main():
    n = int(input())
    s = input()
    assert len(s) == n
    digits = list(s)
    m = [0]
    m.extend(list(map(int, input().split())))
    change = False
    for (i, ch) in enumerate(digits):
        d = int(ch)
        if m[d] > d:
            digits[i] = str(m[d])
            change = True
        elif m[d] < d and change:
            break
    print(''.join(digits))


def __starting_point():
    main()


__starting_point()
