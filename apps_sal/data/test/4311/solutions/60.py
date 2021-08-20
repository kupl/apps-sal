import sys
input = sys.stdin.readline


def main():
    S = int(input())
    x = set()
    x.add(S)
    i = 1
    prev = S
    while True:
        i += 1
        if prev % 2 == 0:
            prev = prev // 2
        else:
            prev = prev * 3 + 1
        if prev in x:
            print(i)
            return
        x.add(prev)


def __starting_point():
    main()


__starting_point()
