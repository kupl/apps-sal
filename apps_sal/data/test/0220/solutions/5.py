'''
Created on Apr 20, 2016
Gmail : r.haque.249@gmail.com
@author: Md. Rezwanul Haque
'''


def func(s, x):
    if x == 0 and s % 2 == 0:
        return 1
    if s == 0:
        return 0
    if (s % 2 == 1 and x % 2 == 1):
        return 2 * func(s // 2, x // 2)
    if (s % 2 == 1 and x % 2 == 0):
        return 0
    if (s % 2 == 0 and x % 2 == 1):
        return 0
    if s % 2 == 0 and x % 2 == 0:
        return func(s // 2 - 1, x // 2) + func(s // 2, x // 2)


s, x = list(map(int, input().split()))
cnt = func(s, x)
if s ^ 0 == x:
    cnt = cnt - 2
print(cnt)
