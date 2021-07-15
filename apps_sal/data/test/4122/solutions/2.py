# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 23:03
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : E. Superhero Battle.py


def main():
    total_hp, n = map(int, input().split())
    d = list(map(int, input().split()))

    c = d.copy()
    for i in range(1, n):
        c[i] += c[i - 1]

    for i in range(n):
        if total_hp + c[i] <= 0:
            print(i + 1)
            return

    if c[-1] >= 0:
        print(-1)
        return

    min_val, round_dmg = -min(c), -c[-1]
    # print(min_val, round_dmg)
    temp_round = (total_hp - min_val + (round_dmg - 1)) // round_dmg
    ret = temp_round * n
    total_hp -= temp_round * round_dmg
    for i in range(n):
        if total_hp + c[i] <= 0:
            ret += i + 1
            break
    print(ret)


def __starting_point():
    main()
__starting_point()
