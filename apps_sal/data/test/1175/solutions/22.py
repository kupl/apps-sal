from functools import lru_cache
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


MOD = 10 ** 9 + 7

"""
桁数が異なると矛盾
したがって商が1であることが必要
すると、xがyのsubsetであることが必要
一番上の桁を含むsubsetがx
"""


@lru_cache()
def F_naive(L, R):
    #
    ret = 0
    ret += F((L + 1) // 2, (R + 1) // 2)  # 2x,2y
    answer = 0
    for x in range(L, R + 1):
        for y in range(x, R + 1):
            if x.bit_length() == y.bit_length() and (x ^ y) + x == y:
                answer += 1
    return answer


@lru_cache()
def F(L, R):
    # x subset y かつ 2x > y
    if L < 0:
        L = 0
    if R < L:
        return 0
    if R == 0:
        return 0
    ret = 0
    # 下一桁が0,0ととる場合
    ret += F((L + 1) // 2, R // 2)
    # 下一桁が0,1ととる場合
    # 2(2x) > (2y+1) iff 2x > y
    ret += F((L + 1) // 2, (R - 1) // 2)
    # 下一桁が1,0ととる場合
    # これはsubsetにならない

    # 下一桁が1,1ととる場合
    # 2(2x+1) > 2y+1 iff 2x >= y
    ret += G(L // 2, (R - 1) // 2)
    return ret


@lru_cache()
def G(L, R):
    # x subset y かつ 2x >= y
    if L < 0:
        L = 0
    if R < L:
        return 0
    if R == 0:
        return 1
    ret = 0
    # 下一桁が0,0ととる場合
    ret += G((L + 1) // 2, R // 2)
    # 下一桁が0,1ととる場合
    # 2(2x) >= (2y+1) iff 2x > y
    ret += F((L + 1) // 2, (R - 1) // 2)
    # 下一桁が1,0ととる場合
    # これはsubsetにならない

    # 下一桁が1,1ととる場合
    # 2(2x+1) >= 2y+1 iff 2x >= y
    ret += G(L // 2, (R - 1) // 2)
    return ret


L, R = map(int, input().split())
answer = F(L, R) % MOD
print(answer)
