from typing import List


def answer(h: int, w: int, a: List[str]) -> List[str]:
    top_bottom_line = '#' * (w + 2)

    result = [top_bottom_line]
    for line in a:
        result.append(f'#{line}#')
    result.append(top_bottom_line)

    return result


def main():
    h, w = list(map(int, input().split()))
    a = [input() for _ in range(h)]
    for i in answer(h, w, a):
        print(i)


def __starting_point():
    main()

__starting_point()
