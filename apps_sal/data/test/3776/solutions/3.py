#! /usr/bin/python
# kmwho


def solvecase():
    form = int(input().strip())
    hh, mm = list(map(int, input().strip().split(":")))
    if mm > 59:
        mm = mm % 10
    if form == 24:
        if hh > 23:
            hh = hh % 10
    elif form == 12:
        if hh > 12:
            if hh % 10:
                hh = hh % 10
            else:
                hh = 10
        if hh == 0:
            hh = 1
    return "%02d:%02d" % (hh, mm)


def main():
    # solve()
    print(solvecase())


main()
