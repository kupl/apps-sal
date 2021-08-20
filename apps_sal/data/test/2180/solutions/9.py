def main():
    lst = ['.' for x in range(0, 500)]
    s = 'C'.join(lst) + 'C'
    lst = ['C' for x in range(0, 500)]
    s_ = '.'.join(lst) + '.'
    n = int(input())
    if n * n % 2 == 0:
        print(n * n // 2)
    else:
        print(n * n // 2 + 1)
    cs = s[:n]
    cs_ = s_[:n]
    flag = True
    for i in range(n):
        if flag:
            print(cs_)
            flag = False
        else:
            print(cs)
            flag = True


def __starting_point():
    main()


__starting_point()
