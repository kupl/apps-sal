#!/usr/bin/env python3


def solve(N: int):
    if N % 2 == 0:
        N = N // 2
        answer = 0
        div = 5
        while N >= div:
            answer += N // div
            div *= 5
        return answer

    else:
        return 0

    return answer


def main():
    N = int(input())
    answer = solve(N)
    print(answer)


def __starting_point():
    main()

__starting_point()
