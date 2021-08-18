import sys
def input(): return sys.stdin.readline().strip()


def d(x):
    if x == 'A':
        return a
    return b


def f(j):
    su = d(s[j])
    for i in range(j + 1, len(s) - 1):
        if s[i] != s[i - 1]:
            su += d(s[i])
    return su


for i in range(int(input())):
    a, b, p = map(int, input().split())
    s = list(input())
    l = -1
    r = len(s) - 1
    while r - l > 1:
        m = (r + l) // 2
        if f(m) > p:
            l = m
        else:
            r = m
    print(r + 1)
