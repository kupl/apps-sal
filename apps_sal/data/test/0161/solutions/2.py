from math import ceil, log2


def __starting_point():
    x = int(input())
    n = []
    c = 0
    count = 0
    while True:
        y = ceil(log2(x))
        y = int(y)
        z = 2**y - 1
        if x == z:
            break
        else:
            if c == 1:
                x += 1
                c = 0
            else:
                x ^= z
                n.append(y)
                c = 1
        count += 1
    print(count)
    print(' '.join(list(map(str, n))))


__starting_point()
