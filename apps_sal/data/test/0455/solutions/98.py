# チェックに漏れがあり、kyasper 11/21 2:28:53のプログラムだと間違い
# ----------
# 例：
# 3
# -2 1
# 1 0
# 1 -2
# ----------

from math import *


def L(xi, di):
    return xi - di


def R(xi, di):
    return xi + di


def D(yi, di):
    return yi - di


def U(yi, di):
    return yi + di


def main():
    N = int(input())
    x_list = [list(map(int, input().split())) for i in range(N)]
    sum_list = [abs(x[0]) + abs(x[1]) for x in x_list]
    checker = sum_list[0] % 2

    for wa in sum_list:
        if wa % 2 != checker:
            print("-1")
            return

    arm_list = []
    if checker == 0:
        arm_list.append(1)

    pow_i = 0
    max_sum = max(sum_list)
    while max_sum > sum(arm_list):
        arm_list.append(2 ** pow_i)
        pow_i += 1
    arm_list = sorted(arm_list, key=lambda x: -x)
    print(len(arm_list))
    print(" ".join(map(str, arm_list)))

    for c in x_list:
        now_c = [0, 0]
        order = ""

        for arm in arm_list:
            dx = c[0] - now_c[0]
            dy = c[1] - now_c[1]

            if abs(dx) > abs(dy):
                if dx > 0:
                    order += "R"
                    now_c[0] = R(now_c[0], arm)
                else:
                    order += "L"
                    now_c[0] = L(now_c[0], arm)
            else:
                if dy > 0:
                    order += "U"
                    now_c[1] = U(now_c[1], arm)
                else:
                    order += "D"
                    now_c[1] = D(now_c[1], arm)
        print(order)


def __starting_point():
    main()


__starting_point()
