def main():
    a, b = list(map(int, input().split()))
    if a >= 13:
        print(b)
    elif a >= 6:
        print((b//2))
    else:
        print((0))

def __starting_point():
    main()

__starting_point()
