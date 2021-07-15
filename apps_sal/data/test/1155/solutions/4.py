import getpass
import sys


def ria():
    return [int(i) for i in input().split()]


files = False

if getpass.getuser() == 'frohenk' and files:
    sys.stdin = open("test.in")

n, m = ria()
mini = 1000
for i in range(n):
    a, b = ria()
    mini = min(mini, a / b)

print(mini*m)
