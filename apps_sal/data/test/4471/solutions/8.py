from sys import stdin, stdout
import math
import heapq
t = 1


def aint():
    return int(input().strip())


def lint():
    return list(map(int, input().split()))


def fint():
    return list(map(int, stdin.readline().split()))


def main():
    n = aint()
    l = lint()
    odd = False
    even = False
    for i in l:
        if i % 2 == 1:
            odd = True
        else:
            even = True
    if odd and even:
        print('NO')
    else:
        print('YES')


t = int(input())
for i in range(t):
    main()
