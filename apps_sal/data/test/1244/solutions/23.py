from collections import Counter


def main():
    n = int(input())
    c = Counter(input().split())
    print(('NO', 'YES')[max(c.values()) * 2 < n + 2])


def __starting_point():
    main()


__starting_point()
