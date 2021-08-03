n = input()


def su(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s


if int('9' * len(n)) <= int(n):
    print(9 * len(n) + su(-int('9' * len(n)) + int(n)))
else:
    if len(n) > 1:
        print(9 * (len(n) - 1) + su(-int('9' * (len(n) - 1)) + int(n)))
    else:
        print(n)
