
def weight(s):
    w, i = 0, 1
    for c in s:
        if c != '=':
            w += i * int(c)
        i += 1
    return w


def main():
    line = input()
    l, r = line.split('^')
    l = weight(l[::-1])
    r = weight(r)
    if l > r:
        print('left')
    elif l < r:
        print('right')
    else:
        print('balance')


def __starting_point():
    main()


__starting_point()
