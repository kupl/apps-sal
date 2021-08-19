import re


def __starting_point():
    x = int(input())
    s = input()
    (zeros, ones) = (0, 0)
    for char in s:
        if char == '0':
            zeros += 1
        if char == '1':
            ones += 1
    print(abs(zeros - ones))


__starting_point()
