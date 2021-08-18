import getpass
import sys


def ria():
    return [int(i) for i in input().split()]


if getpass.getuser() != 'frohenk':
    filename = 'half'
else:
    sys.stdin = open('input.txt')

n = ria()[0]
print(n)
print('1 ' * n)
