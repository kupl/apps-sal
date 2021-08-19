def main():
    n = int(input())
    if n > -10:
        print(n)
    else:
        n = str(n * -1)
        l = len(n)
        print(min(int(n[:l - 1]), int(n[:l - 2] + n[l - 1])) * -1)


main()
