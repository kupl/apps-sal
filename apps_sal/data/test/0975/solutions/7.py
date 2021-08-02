import math
import sys


def main():
    n = int(input())
    s1 = list(input().strip())
    s2 = list(input().strip())
    sort2 = sorted(s2)
    sort1 = sorted(s1)
    # print(sort1)
    # print(sort2)
    maxs = 0;
    j = 0
    for i in range(n):
        while(j != n and sort1[i] >= sort2[j]):
            j += 1
        if (j == n):
            break
        j += 1
        maxs += 1

    j = 0
    mins = 0
    for i in range(n):
        while(j != n and sort1[i] > sort2[j]):
            j += 1
            mins += 1
        if (j == n):
            break
        j += 1
    print(mins)
    print(maxs)


def __starting_point():
    main()


__starting_point()
