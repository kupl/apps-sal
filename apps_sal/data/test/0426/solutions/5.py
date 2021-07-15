import random
import sys


def get_many_ints():
    return list(map(int, input().split()))


def get_int():
    return int(input())


N, K = get_many_ints()
S = list(input())

if N == 1 and K > 0:
    print("0")
    return

if K > 0:
    if S[0] != "1":
        S[0] = "1"
        K -= 1
    for i in range(1, N):
        if S[i] != "0" and K > 0:
            K -= 1
            S[i] = "0"

print("".join(S))

