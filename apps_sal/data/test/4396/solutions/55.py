from typing import List, Tuple


def answer(n: int, xus: List[Tuple[float, str]]) -> float:
    otoshidama = 0
    for (x, u) in xus:
        if u == 'BTC':
            otoshidama += x * 380000.0
        else:
            otoshidama += x
    return otoshidama


def main():
    n = int(input())
    xus = []
    for i in range(n):
        (x, u) = input().split()
        xus.append((float(x), u))
    print(answer(n, xus))


def __starting_point():
    main()


__starting_point()
