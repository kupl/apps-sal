import sys
from collections import Counter
stdin = sys.stdin


def ns():
    return stdin.readline().rstrip()


def ni():
    return int(stdin.readline().rstrip())


def nm():
    return list(map(int, stdin.readline().split()))


def nl():
    return list(map(int, stdin.readline().split()))


def get_ans(v, ans):
    while len(v) != 1:
        ans += v.pop()
    return ans


def main():
    n = ni()
    V = nl()
    V_e = V[0::2]
    V_o = V[1::2]
    V_e_c = Counter(V_e)
    V_o_c = Counter(V_o)
    if V_e_c.most_common()[0][0] != V_o_c.most_common()[0][0]:
        ans = len(V) - V_e_c.most_common()[0][1] - V_o_c.most_common()[0][1]
    elif len(V_e_c.most_common()) == 1 or len(V_o_c.most_common()) == 1:
        if len(V_e_c.most_common()) == 1 and len(V_o_c.most_common()) == 1:
            ans = len(V) // 2
        elif len(V_e_c.most_common()) != 1:
            ans = len(V) // 2 - V_e_c.most_common()[1][1]
        else:
            ans = len(V) // 2 - V_o_c.most_common()[1][1]
    else:
        ans = len(V) - max(V_e_c.most_common()[0][1] + V_o_c.most_common()[1][1], V_e_c.most_common()[1][1] + V_o_c.most_common()[0][1])
    print(ans)


def __starting_point():
    main()


__starting_point()
