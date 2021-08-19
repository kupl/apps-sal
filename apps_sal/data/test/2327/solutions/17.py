import math


def check(a):
    count = 0
    i = 1
    while i <= a:
        count = count + a // i
        i *= 2
    return count


for _ in range(int(input())):
    a = int(input())
    print(check(a))
