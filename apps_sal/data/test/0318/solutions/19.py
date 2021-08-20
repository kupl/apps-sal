def main():
    mode = 'filee'
    if mode == 'file':
        f = open('test.txt', 'r')

    def get():
        return [int(x) for x in (f.readline() if mode == 'file' else input()).split(':')]
    [h, m] = get()
    [n] = get()
    x = h * 60 + m
    x = (x + n) % 1440
    print(str(x // 60).rjust(2, '0') + ':', end='')
    print(str(x % 60).rjust(2, '0'))
    if mode == 'file':
        f.close()


def __starting_point():
    main()


__starting_point()
