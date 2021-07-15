import getpass
import sys


def ria():
    return [int(i) for i in input().split()]


if getpass.getuser() != 'frohenk':
    filename = 'half'
    # sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w')
else:
    sys.stdin = open('input.txt')
    # sys.stdin.close()

crd = input()
cs = input().split()
for i in cs:
    if i[0] == crd[0] or i[1] == crd[1]:
        print('YES')
        return

print('NO')

