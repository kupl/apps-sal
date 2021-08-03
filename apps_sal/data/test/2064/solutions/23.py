def main():
    n = int(input())
    if n % 2 == 0:
        print('1' * (n // 2))
    else:
        print(7, end='')
        if n > 3:
            print('1' * (n // 2 - 1))


main()
