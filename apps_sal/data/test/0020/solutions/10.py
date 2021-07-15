# coding: utf-8

def is_parindrome(h, m):
    s = "{:02d}:{:02d}".format(h, m)
    return s == s[::-1]


def main():
    h, m = list(map(int, input().split(":")))
    c = 0
    while not is_parindrome(h, m):
        m += 1
        c += 1
        if m == 60:
            h += 1
            m = 0
            if h == 24:
                h = 0
    return c


print(main())

