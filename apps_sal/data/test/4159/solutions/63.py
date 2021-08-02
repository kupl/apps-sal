#!/usr/bin/env python


def solve(A: int, B: int, K: int):
    if A >= K:
        return f"{A-K} {B}"
    elif A + B >= K:
        return f"0 {A+B-K}"
    else:
        return "0 0"


def main():
    A, B, K = list(map(int, input().split()))
    answer = solve(A, B, K)
    print(answer)


def __starting_point():
    main()


__starting_point()
