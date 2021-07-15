def main():
    n = int(input())
    cont = 0
    for _ in range(n):
        a, b = input().split()
        if a == b:
            cont += 1
            if cont >= 3:
                print('Yes')
                return
        else:
            cont = 0

    print('No')


def __starting_point():
    main()

__starting_point()
