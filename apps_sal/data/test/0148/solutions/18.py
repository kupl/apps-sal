import sys
input = sys.stdin.readline


def ii():
    return int(input())


def mi():
    return list(map(int, input().rstrip().split()))


def lmi():
    return list(map(int, input().rstrip().split()))


def li():
    return list(input().rstrip())


def __starting_point():
    (n, a, x, b, y) = mi()
    while a % n != x % n and b % n != y % n:
        a += 1
        a %= n
        b -= 1
        b %= n
        if a % n == b % n:
            print('YES')
            break
    else:
        print('NO')


__starting_point()
