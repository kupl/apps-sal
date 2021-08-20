import math


def main():
    (H, W) = [int(a) for a in input().split(' ')]
    cand = []
    if W % 3 == 0 or H % 3 == 0:
        print(0)
        return 0
    cand.append(H)
    cand.append(W)
    cand += split_3(H, W)
    cand += split_3(W, H)
    print(min(cand))
    return 0


def split_3(a, b):
    a_f = math.floor(a / 3)
    a_c = math.ceil(a / 3)
    b_f = math.floor(b / 2)
    b_c = math.ceil(b / 2)
    a1 = [b * a_f, (a - a_f) * b_f, a * b - (a - a_f) * b_f - b * a_f]
    a2 = [b * a_c, (a - a_c) * b_f, a * b - (a - a_c) * b_f - b * a_c]
    a3 = [b * a_f, (a - a_f) * b_c, a * b - (a - a_f) * b_c - b * a_f]
    a4 = [b * a_c, (a - a_c) * b_c, a * b - (a - a_c) * b_c - b * a_c]
    return [max(a1) - min(a1), max(a2) - min(a2), max(a3) - min(a3), max(a4) - min(a4)]


main()
