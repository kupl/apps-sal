#!/usr/bin/env python3
def main():
    _ = int(input())
    S = input()

    ans = 0
    res = ""
    for s in S:
        if res == s:
            continue
        res = s
        ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
