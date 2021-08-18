def main():
    n, m = input().split(' ')
    n, m = int(n), int(m)
    str1 = '
    str2 = '.' * (m - 1) + '
    str3 = '
    for i in range(1, n + 1):
        if (i - 2) % 4 == 0:
            print(str2)
        elif i % 4 == 0:
            print(str3)
        else:
            print(str1)


main()
