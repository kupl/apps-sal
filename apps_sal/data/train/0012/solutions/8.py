import math


def main():
    was = set()
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        if a[i] - b[i] > 0:
            if not -1 in was:
                print('NO')
                return
        elif a[i] - b[i] < 0:
            if not 1 in was:
                print('NO')
                return
        was.add(a[i])
    print('YES')


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
