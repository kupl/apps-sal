#!/usr/bin/env python


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = list(reversed(b))
    bad = next((x for x, y in zip(a, b) if x == y), None)
    if bad is None:
        print('Yes')
        print((' '.join(map(str, b))))
    else:
        l_1 = sum(1 for x, y in zip(a, b) if x < bad < y)
        l_2 = sum(1 for x, y in zip(a, b) if x < y and bad in (x, y))
        l_3 = sum(1 for x, y in zip(a, b) if x == y)
        l_4 = sum(1 for x, y in zip(a, b) if x > y and bad in (x, y))
        l_5 = sum(1 for x, y in zip(a, b) if x > bad > y and x != bad)
        if l_3 > l_1 + l_5:
            print('No')
        else:
            good_part = b[:l_1] + b[l_1 + l_2 + l_3 + l_4:]
            bad_part = b[l_1 + l_2:l_1 + l_2 + l_3]
            b[l_1 + l_2:l_1 + l_2 + l_3] = good_part[:l_3]
            good_part[:l_3] = bad_part
            b[:l_1] = good_part[:l_1]
            b[l_1 + l_2 + l_3 + l_4:] = good_part[l_1:]
            assert all(x != y for x, y in zip(a, b))
            print('Yes')
            print((' '.join(map(str, b))))


def __starting_point():
    main()


__starting_point()
