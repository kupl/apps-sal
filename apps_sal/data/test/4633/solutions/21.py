from math import ceil
from collections import deque


def sm(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret


for _ in range(int(input())):
    n, s = [int(i) for i in input().split()]
    temp = n
    while sm(n) > s:
        j = 10
        while n % j == 0:
            j *= 10
        n += j - n % j
    print(n - temp)
