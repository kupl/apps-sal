
def main():
    ab = int(input().replace(" ", ""))
    print(("Yes" if int(ab**.5)**2 == ab else "No"))


def __starting_point():
    main()


__starting_point()
