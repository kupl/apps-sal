def main():
    a, b = list(map(int, input().split()))
    if a == b:
        print(0)
    elif a > b:
        if (b - a) % 2 == 0:
            print(1)
        else:
            print(2)
    else:
        if (b - a) % 2 == 0:
            print(2)
        else:
            print(1)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()

__starting_point()
