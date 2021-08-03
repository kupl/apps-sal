
import sys


def input():

    return sys.stdin.readline()


for _ in range(int(input())):

    n = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    x = 10 ** 9
    y = 0
    while x > y + 1:

        z = (x + y) // 2

        t = 0

        for i in range(n):
            if A[i] > z:
                t += B[i]

        if t > z:
            y = z

        else:
            x = z

    print(x)
