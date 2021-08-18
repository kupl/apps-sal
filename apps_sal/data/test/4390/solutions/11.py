

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        if a % b == 0:
            print(0)
        else:
            print(b - a % b)
    return


def __starting_point():
    main()


__starting_point()
