import sys
import math


def mp():
    return list(map(int, input().split()))


def main():
    n = int(input())
    a = input()
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            print(a[:i] + a[i + 1:])
            return
    print(a[:len(a) - 1])


main()
