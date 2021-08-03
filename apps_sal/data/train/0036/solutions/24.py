from sys import stdin
from bisect import bisect_left


def main():
    stdin.readline()
    x, a = 0, []
    for y in map(int, stdin.readline().split()):
        x += y
        a.append(x)

    stdin.readline()
    for x in map(int, stdin.readline().split()):
        print(bisect_left(a, x) + 1)


main()
