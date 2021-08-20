def main():
    n = int(input())
    lst = input()
    if n % 2 == 0:
        for i in range(1, n, 2):
            if int(lst[i]) % 2 == 0:
                print('2')
                return
        print('1')
        return
    for i in range(0, n, 2):
        if int(lst[i]) % 2 == 1:
            print('1')
            return
    print('2')
    return


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
