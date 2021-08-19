# coding: utf-8

n, mp = list(map(int, input().split(" ")))
a_list = list(map(int, input().split(" ")))
b_list = list(map(int, input().split(" ")))


def bake(mp):
    minus = 0
    for i in range(n):
        b_list[i] -= a_list[i]
        if b_list[i] < 0:
            minus += b_list[i]
            b_list[i] = 0
    mp += minus
    if mp >= 0:
        return 1, mp
    else:
        return 0, mp


def init_bake():
    c = min([b // a for a, b in zip(a_list, b_list)])
    for i in range(n):
        b_list[i] -= a_list[i] * c
    return c


cookies = init_bake()
while True:
    c, mp = bake(mp)
    if c == 0:
        break
    cookies += c

print(cookies)
