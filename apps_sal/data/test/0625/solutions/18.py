def main():
    n = int(input())
    if n % 2 == 0:
        res = int(n / 2)
    else:
        res = int(-n / 2 - 1)
    print(res)


main()
