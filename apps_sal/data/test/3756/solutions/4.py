def main():
    n, t = map(int, input().split())
    b = input()
    p = b.find('.')
    for i in range(p + 1, n):
        if b[i] > '4':
            break
    else:
        print(b)
        return

    while t:
        i -= 1
        t -= 1
        if b[i] < '4':
            break
    if i > p:
        print(b[:i], chr(ord(b[i]) + 1), sep='')
    else:
        k = list(b[:i])
        for x in range(len(k) - 1, -1, -1):
            if k[x] == '9':
                k[x] = '0'
            else:
                k[x] = chr(ord(k[x]) + 1)
                break
        else:
            k.insert(0, '1')
        print(''.join(k))


def __starting_point():
    main()


__starting_point()
