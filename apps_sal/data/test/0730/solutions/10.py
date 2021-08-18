def main():
    n = int(input())
    print("+------------------------+")
    b1 = 0
    if n == 0:
        b1 = 0
    elif 1 <= n <= 4:
        b1 = 1
    else:
        b1 = (n + 1) // 3
    if 0 <= n <= 1:
        b2 = 0
    elif 2 <= n <= 5:
        b2 = 1
    else:
        b2 = n // 3
    b3 = 0
    if n < 3:
        b3 = 0
    else:
        b3 = 1
    b4 = 0
    if n <= 3:
        b4 = 0
    else:
        b4 = (n - 1) // 3
    print("|", end='')
    for i in range(1, 12):
        if i <= b1:
            print('O.', end='')
        else:
            print('
    print('|D|)')
    print("|", end='')
    for i in range(1, 12):
        if i <= b2:
            print('O.', end='')
        else:
            print('
    print('|.|')
    if b3 == 0:
        print("|
    else:
        print("|O.......................|")
    print("|", end='')
    for i in range(1, 12):
        if i <= b4:
            print('O.', end='')
        else:
            print('
    print('|.|)')
    print("+------------------------+")


main()
