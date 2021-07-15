#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()

    res = ord('A')
    ans = ''
    for s in S:
        ans += chr(res + (ord(s) - res + N) % 26)
    print(ans)


def __starting_point():
    main()

__starting_point()
