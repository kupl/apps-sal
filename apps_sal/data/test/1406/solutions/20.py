# -*- coding: utf-8 -*-
import sys


def main():
    n, k, d = map(int, sys.stdin.readline().split())

    blocksize = n

    for i in range(d):
        blocksize = blocksize // k + (blocksize % k != 0)
    # print(blocksize)

    if(blocksize > 1):
        print("-1")
        return

    for days in range(d):
        i = 0
        bus = 1
        while i < n:
            for j in range(blocksize):
                sys.stdout.write(str(bus) + ' ')
                i += 1
                if i == n:
                    break
            bus += 1
            if(bus > k):
                bus = 1
        blocksize *= k
        sys.stdout.write('\n')


def __starting_point():
    main()


__starting_point()
