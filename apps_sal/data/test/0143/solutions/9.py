import sys


def main():
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    x.sort()
    c = 1
    for i in range(n):
        if x[i] >= c:
            c += 1
    print(c)


main()
