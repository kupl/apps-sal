from typing import List


def answer(n: int, s: List[int]) -> int:
    ans = 0
    not_multiples_of_10 = []
    for i in s:
        ans += i
        if i % 10 != 0:
            not_multiples_of_10.append(i)
    if not not_multiples_of_10:
        return 0
    if ans % 10 == 0:
        ans = ans - min(not_multiples_of_10)
    return ans


def main():
    n = int(input())
    s = [int(input()) for _ in range(n)]
    print(answer(n, s))


def __starting_point():
    main()


__starting_point()
