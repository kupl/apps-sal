import math
import sys


def chek(m, b, c, li):
    for i in range(li):
        if m[i] + b[i] > c:
            return False
    return True


def input(): return sys.stdin.readline().rstrip()


f = int(input())
for _ in range(f):
    a, b = list(map(int, input().split()))
    s = input()
    mas = []
    c = 1
    k = len(s)
    cur = 1
    while c != k:
        if s[c] == s[c - 1]:
            cur += 1
        else:
            if len(mas) != 0:
                mas.append(cur)
                cur = 1
            else:
                if s[c] == "0":
                    mas.append(cur)
                    cur = 1
                else:
                    cur = 1
        c += 1
    if s[c - 1] == "1":
        mas.append(cur)
    ans = 0
    for i in range(len(mas)):
        if i % 2 == 0:
            ans += a
        else:
            if a > b * mas[i]:
                ans += b * mas[i]
                ans -= a
    print(ans)
