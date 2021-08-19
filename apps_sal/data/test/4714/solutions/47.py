def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def main():
    (a, b) = Input()
    ans = 0
    for i in range(a, b + 1):
        str_i = list(str(i))
        if str_i[0] == str_i[-1] and str_i[1] == str_i[-2]:
            ans += 1
    print(ans)


main()
