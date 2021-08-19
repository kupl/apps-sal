def alp_num(alp):
    alp_lst = list('ABCDEF')
    num = alp_lst.index(alp)
    return num


def main():
    (x, y) = map(str, input().split())
    num1 = alp_num(x)
    num2 = alp_num(y)
    if num1 < num2:
        com_ope = '<'
    elif num1 == num2:
        com_ope = '='
    else:
        com_ope = '>'
    print(com_ope)


def __starting_point():
    main()


__starting_point()
