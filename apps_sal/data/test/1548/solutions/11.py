import sys


def main():
    n = int(input())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)
    x = y = 0
    i = 0
    while i < n - i - 1:
        x += a[i]
        y += a[n - i - 1]
        i += 1
    if (n % 2):
        x += a[i]
    print(x * x + y * y)


main()
