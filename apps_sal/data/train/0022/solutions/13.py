import sys


def pprint(s):
    return print(' '.join(map(str, s)))


def input():
    return sys.stdin.readline().strip()


ipnut = input
for i in range(int(input())):
    (a, k) = map(int, input().split())
    for i in range(k - 1):
        x = list(map(int, str(a)))
        a_i = min(x)
        a_m = max(x)
        a = a + a_i * a_m
        if a_i == 0:
            break
    print(a)
'\n10\n10 11 12 13 14 15 16 17 11 11\n'
