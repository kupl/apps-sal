def main():
    s = input().split()
    n = int(s[0])
    l = int(s[1])
    r = int(s[2])
    s = input().split()
    arr1 = []
    for i in range(n):
        k = int(s[i])
        arr1.append(k)
    s = input().split()
    for i in range(n):
        k = int(s[i])
        if arr1[i] != k and (i + 1 < l or i + 1 > r):
            print('LIE')
            return
    print('TRUTH')
    return


def __starting_point():
    main()


__starting_point()
