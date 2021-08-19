import sys


def main():
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    i = 0
    n += 1
    x = [0] + x + [0]
    while i < n and x[i] < x[i + 1]:
        i += 1
    while i < n and x[i] == x[i + 1]:
        i += 1
    while i < n and x[i] > x[i + 1]:
        i += 1
    if i == n:
        print('YES')
    else:
        print('NO')


main()
