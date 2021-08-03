import sys
input = sys.stdin.readline

q = int(input())


def calc(n):
    for i in range(40):
        if n <= 3**i:
            break

    if n == 3**i:
        return n

    elif n > (3**i - 1) // 2:
        return 3**i

    else:
        n -= 3**(i - 1)
        return 3**(i - 1) + calc(n)


for testcases in range(q):
    n = int(input())
    print(calc(n))
