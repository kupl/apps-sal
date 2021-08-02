n = input()
a = list(map(int, input().split()))


def main():
    a.sort()

    b = w = 0

    for i, x in enumerate(a):
        x -= 1

        b += abs(2 * i - x)
        w += abs(2 * i + 1 - x)

    print(min(b, w))


main()
