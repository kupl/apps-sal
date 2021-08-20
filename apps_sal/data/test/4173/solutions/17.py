from sys import stdin, stdout


def inp():
    return (int(o) for o in stdin.readline().split())


def sinp():
    return (o for o in stdin.readline().split())


def out():
    return stdout.write(str())


def I():
    return map(int, input().split())


def Y():
    return int(input())


for _ in range(int(input())):
    (n, a, b) = I()
    if 2 * a < b:
        print(n * a)
    else:
        print(n // 2 * b + n % 2 * a)
