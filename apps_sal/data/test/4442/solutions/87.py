#!/usr/bin/env python3
def main():
    a, b = list(map(int, input().split()))

    can_a = str(a) * b
    can_b = str(b) * a
    if can_a < can_b:
        print(can_a)
    else:
        print(can_b)


def __starting_point():
    main()

__starting_point()
