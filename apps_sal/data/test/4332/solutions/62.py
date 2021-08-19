def main():
    n = input()
    if int(n) % sum(map(int, list(n))) == 0:
        print('Yes')
    else:
        print('No')


main()
