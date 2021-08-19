import sys


def I():
    return list(map(int, input().split()))


def sieve(n):
    a = [1] * n
    for i in range(2, n):
        if a[i]:
            for j in range(i * i, n, i):
                a[j] = 0
    return a


for __ in range(int(input())):
    s = input()
    if min(s.count('0'), s.count('1')) % 2 == 0:
        print('NET')
    else:
        print('DA')
