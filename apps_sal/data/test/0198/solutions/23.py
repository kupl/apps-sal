def main():
    n = int(input())
    if n > 6 and n % 2 == 0:
        print(int((n // 2 - 1) / 2))
    elif n == 6:
        print(1)
    else:
        print(0)

def __starting_point():
    main()
__starting_point()
