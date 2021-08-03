import math
import sys


def mp():
    return list(map(int, input().split()))


def main():
    n = int(input())
    for i in range(n):
        a = list(input().strip())
        a.sort()
        if a[0] == a[-1]:
            print(-1)
        else:
            print(''.join(a))


deb = 0
if deb:
    file = open('input.txt', 'w')
else:
    input = sys.stdin.readline

main()
