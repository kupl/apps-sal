#!/usr/bin/env python3


def main():
    N, K, *L = list(map(int, open(0).read().split()))
    L.sort()
    print((sum(L[-K:])))


main()

