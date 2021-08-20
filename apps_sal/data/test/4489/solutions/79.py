from typing import List


def answer(n: int, s: List[str], m: int, t: List[str]) -> int:
    result = 0
    for i in s:
        result = max(result, s.count(i) - t.count(i))
    return result


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    m = int(input())
    t = [input() for _ in range(m)]
    print(answer(n, s, m, t))


def __starting_point():
    main()


__starting_point()
