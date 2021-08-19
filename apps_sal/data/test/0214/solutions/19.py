def main():
    (a, b) = ([i for i in input()], [i for i in input()])
    l = len(a)
    c = 0
    for i in range(l - 1):
        if a[i] == '0':
            if b[i] == '0':
                if a[i + 1] == '0':
                    c += 1
                    (a[i], b[i], a[i + 1]) = (1, 1, 1)
                elif b[i + 1] == '0':
                    c += 1
                    (a[i], b[i], b[i + 1]) = (1, 1, 1)
            elif a[i + 1] == '0' and b[i + 1] == '0':
                c += 1
                (a[i], a[i + 1], b[i + 1]) = (1, 1, 1)
        elif b[i] == '0' and b[i + 1] == '0' and (a[i + 1] == '0'):
            c += 1
            (b[i], a[i + 1], b[i + 1]) = (1, 1, 1)
    print(c)
    return 0


main()
