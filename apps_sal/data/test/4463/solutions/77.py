#!/usr/bin/env python3


def main():
    s = sorted(input())
    t = sorted(input(), reverse=True)
    if s < t:
        print("Yes")
    else:
        print("No")


main()
