import sys


def main():
    (n, x) = list(map(int, sys.stdin.readline().split()))
    if n < 3:
        print(1)
        return 0
    print((n - 2 + x - 1) // x + 1)


for i in range(int(sys.stdin.readline().strip())):
    main()
