i = input()
if (int(i) % 2) == 0:
    while int(i) > 0:
        i = int(i) - 2
        print(1, end='')
else:
    print(7, end='')
    i = int(i) - 3
    while int(i) > 0:
        i = int(i) - 2
        print(1, end='')
