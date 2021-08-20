import math
from datetime import date


def main():
    line = input().split()
    a = [int(x) for x in line]
    a.sort()
    if a[0] == 5 and a[1] == 5 and (a[2] == 7):
        print('YES')
    else:
        print('NO')


main()
