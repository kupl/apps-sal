import sys


def main():
    (h, w) = map(int, input().split())
    if h % 3 == 0 or w % 3 == 0:
        print(0)
        return
    pattern = [h, w]
    for x in range(1, w // 2 + 2):
        first = x * h
        h1 = h // 2
        h2 = h - h1
        second = (w - x) * h1
        thrid = (w - x) * h2
        result = max(first, second, thrid) - min(first, second, thrid)
        pattern.append(result)
    for y in range(1, h // 2 + 2):
        first = y * w
        w1 = w // 2
        w2 = w - w1
        second = (h - y) * w1
        thrid = (h - y) * w2
        result = max(first, second, thrid) - min(first, second, thrid)
        pattern.append(result)
    print(min(pattern))


def __starting_point():
    main()


__starting_point()
