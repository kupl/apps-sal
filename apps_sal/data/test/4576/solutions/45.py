import sys
input = sys.stdin.readline


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    target = int(input())
    count = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if 500 * i + 100 * j + 50 * k == target:
                    count += 1
                else:
                    continue
    print(count)


def __starting_point():
    main()


__starting_point()
