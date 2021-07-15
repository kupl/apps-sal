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

cache = {}
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp // i in cache:
            arr = cache[temp // i]
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    cache[n] = arr
    return arr

def main():
    N = input_int()

    cnt = 0
    for a in range(1, N):
        for b in range(1, N):
            if a * b - N < 0:
                cnt += 1
            else:
                break

    print(cnt)


def __starting_point():
    main()

__starting_point()
