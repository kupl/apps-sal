#!/usr/bin/env python3
def main():
    N = int(input())

    candidate = []
    for divisor in range(1, int(N ** 0.5) + 1):
        if N % divisor == 0:
            candidate.append((divisor, N // divisor))
    ans = min([a + b - 2 for a, b in candidate])
    print(ans)


def __starting_point():
    main()

__starting_point()
