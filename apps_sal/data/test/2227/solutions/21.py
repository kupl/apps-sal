
import re


def main():
    l = input()

    heavyCnt = 0
    res = 0
    for i in range(4, len(l)):
        if l[i - 4: i + 1] == "heavy":
            heavyCnt += 1
        if l[i - 4: i + 1] == "metal":
            res += heavyCnt

    print(res)


def __starting_point():
    main()


__starting_point()
