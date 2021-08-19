def main():
    input()
    aa = input().split()
    bb = input().split()
    aa.remove('0')
    bb.remove('0')
    a = aa.index('1')
    b = bb.index('1')
    print(('NO', 'YES')[aa[a:] + aa[:a] == bb[b:] + bb[:b]])


def __starting_point():
    main()


__starting_point()
