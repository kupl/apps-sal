
def main():
    input()
    arr = list(map(int, input().split()))
    if arr.count(1):
        print('HARD')
    else:
        print('EASY')


def __starting_point():
    main()


__starting_point()
