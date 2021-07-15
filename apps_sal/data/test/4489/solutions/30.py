#!/usr/bin/env python3

def main():
    blue = [input() for i in range(int(input()))]
    red = [input() for i in range(int(input()))]
    l = list(set(blue))
    print((max(0, max(blue.count(l[i]) - red.count(l[i]) for i in range(len(l))))))


def __starting_point():
    main()

__starting_point()
