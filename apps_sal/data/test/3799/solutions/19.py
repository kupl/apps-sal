import collections


def solve():
    s = input()
    if s[0] == s[-1]:
        if len(s) % 2 == 0:
            print("First")
        else:
            print("Second")
    else:
        if len(s) % 2 == 0:
            print("Second")
        else:
            print("First")


def __starting_point():
    solve()


__starting_point()
