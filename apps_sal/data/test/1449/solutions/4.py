"""

"""
from sys import stdin


def updiv(a, b):
    if a % b == 0:
        return a // b
    else:
        return a // b + 1


tt = int(stdin.readline())
for loop in range(tt):
    (n, k) = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    num = 0
    for i in range(n):
        if i == 0:
            num += 1
        elif a[i] != a[i - 1]:
            num += 1
    if k == 1:
        if num == 1:
            print(1)
        else:
            print(-1)
        continue
    elif num <= k:
        print(1)
        continue
    num -= k
    print(updiv(num, k - 1) + 1)
