from typing import List


def answer(h: int, w: int, a: List[str]) -> List[str]:
    for i in range(2):
        white_line = '.' * w
        loop = a.count(white_line)
        for _ in range(loop):
            a.remove(white_line)
        a = [''.join(line) for line in (list(zip(*a)))]
        if i == 0:
            w = h - loop

    return a


def main():
    h, w = list(map(int, input().split()))
    a = [input() for _ in range(h)]
    for i in answer(h, w, a):
        print(i)


def __starting_point():
    main()


__starting_point()
