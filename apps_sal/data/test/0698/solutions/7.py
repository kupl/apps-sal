

def main():
    x, t = list(map(int, input().split()))
    markers = [1] * (x - 1)
    for c in range(t):
        r = [int(n) for n in input().split()]
        markers[r[1] - 1] = 0
        if r[0] == 1:
            markers[r[2] - 1] = 0
    c = 0
    max_num = 0
    min_num = 0
    for i in markers:
        if i:
            c += 1
            continue
        if c:
            max_num += c
            min_num += ((c + 1) >> 1)
        c = 0
    if c:
        max_num += c
        min_num += ((c + 1) >> 1)
    print(min_num, max_num)


def __starting_point():
    main()


__starting_point()
