#!/usr/bin/env python3
def main():
    S = input()

    ans = 0
    for i in range(len(S)):
        if S[i] != S[-(i + 1)]:
            ans += 1
    print((ans // 2))


def __starting_point():
    main()

__starting_point()
