import sys


def main():
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    found = True
    while found:
        found = False
        for i in range(1, n):
            if x[i] < x[i - 1]:
                found = True
                print(i, i + 1)
                (x[i - 1], x[i]) = (x[i], x[i - 1])


main()
