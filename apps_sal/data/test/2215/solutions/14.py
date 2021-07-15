import sys
import os

def sonyaAndExhibition(n, m, visitors):
    return ('01' * n)[:n]

def main():
    n, m = (int(x) for x in input().split())
    visitors = []
    for i in range(m):
        l, r = (int(x) for x in input().split())
        visitors.append((l, r))
    print(sonyaAndExhibition(n, m, visitors))

def __starting_point():
    main()
__starting_point()
