from sys import stdin, stdout


def rint():
    return map(int, stdin.readline().split())


n = int(input())
if n == 0:
    print(0)
elif n % 2:
    print((n + 1) // 2)
else:
    print(n + 1)
