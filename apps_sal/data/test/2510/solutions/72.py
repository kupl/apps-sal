# -*- coding: utf-8 -*-

# 入力を整数に変換して受け取る
def input_int():
    return int(input())


# マイナス1した値を返却
def int1(x):
    return int(x) - 1


# 半角スペース区切り入力をIntに変換してMapで受け取る
def input_to_int_map():
    return list(map(int, input().split()))


# 半角スペース区切り入力をIntに変換して受け取る
def input_to_int_tuple():
    return tuple(map(int, input().split()))


# 半角スペース区切り入力をIntに変換してマイナス1した値を受け取る
def input_to_int_tuple_minus1():
    return tuple(map(int1, input().split()))


def main():
    N, M = input_to_int_map()
    AB = (input_to_int_tuple() for i in range(M))

    from collections import defaultdict
    friends = defaultdict(lambda: -1)

    def root(x):
        temp = friends[x]
        if temp < 0:
            return x
        temp2 = root(temp)
        friends[x] = temp2
        return temp2

    for a, b in AB:
        a = root(a)
        b = root(b)
        if a == b:
            continue

        if (friends[a] > friends[b]):
            temp = a
            a = b
            b = temp
        friends[a] += friends[b]
        friends[b] = a

    ret = 0
    for i in range(1, N + 1):
        temp = root(i)
        ret = max(ret, -friends[temp])

    print(ret)


def __starting_point():
    main()


__starting_point()
