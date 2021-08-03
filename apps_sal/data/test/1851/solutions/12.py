import sys


def input():
    return sys.stdin.readline().strip()


def print(*x, sep=' ', end='\n'):
    return sys.stdout.write(sep.join(map(str, x)) + end)


def read():
    return sys.stdin.read()


def get():
    return int(input()), [int(i) for i in input().split()]


def out(*arg):
    if type(arg[0]) == list:
        for i in arg[0]:
            print(i)
    else:
        print(arg)


def main():
    n, ls = get()
    stack = -1
    ans = 0
    for i in range(n):
        stack = max(ls[i], i + 1, stack)
        if stack == i + 1:
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
