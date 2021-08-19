def main():
    mode = 'filee'
    if mode == 'file':
        f = open('test.txt', 'r')

    def get():
        return [int(x) for x in (f.readline() if mode == 'file' else input()).split()]
    [n, k] = get()
    a = get()
    b = []
    s = 0
    for i in a:
        if i == 100:
            s += 10
            continue
        b.append([i % 10, i])
    b.sort()
    b.reverse()
    if len(b) > 0 and k > 0:
        for i in b:
            if k >= 10 - i[0]:
                hold = min(10 - i[0], k)
                k -= hold
                i[1] += hold
                i[0] += hold
            else:
                k = 0
                break
    if k > 0 and len(b) > 0:
        k -= k % 10
        for i in b:
            if i[1] == 100:
                continue
            if k == 0:
                break
            hold = min(100 - i[1], k)
            k -= hold
            i[1] += hold
    for i in b:
        s += i[1] // 10
    print(s)
    if mode == 'file':
        f.close()


def __starting_point():
    main()


__starting_point()
