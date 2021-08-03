#!/usr/bin/env python3

def main():
    H, W = list(map(int, input().split()))
    h, w = list(map(int, input().split()))
    print(((H - h) * (W - w)))


def __starting_point():
    main()


__starting_point()
