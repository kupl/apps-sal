
def main():
    antenna = [int(input()) for i in range(5)]
    k = int(input())
    print((":(" if max(antenna) - min(antenna) > k else "Yay!"))


def __starting_point():
    main()


__starting_point()
