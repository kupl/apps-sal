#!/usr/bin/env python3

#                 N    N'
#   | 1  2  3  4  5
# 1 | 1  2  3  4  5 :  N // 1   1 * N' (N'+1) // 2
# 2 |    2     4    :  N // 2   2 * N' (N'+1) // 2
# 3 |       3       :  N // 3   3 * N' (N'+1) // 2
# 4 |          4    :  N // 4   4 * N' (N'+1) // 2
# 5 |             5 :  N // 5   5 * N' (N'+1) // 2


def solve(N):
    answer = 0
    for i in range(1, N + 1):
        mprime = N // i
        answer += i * (mprime * (mprime + 1)) // 2
    return answer


def main():
    N = int(input())  # type: int
    answer = solve(N)
    print(answer)


def __starting_point():
    main()


__starting_point()
