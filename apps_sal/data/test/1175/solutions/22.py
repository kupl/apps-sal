from functools import lru_cache
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
'\n桁数が異なると矛盾\nしたがって商が1であることが必要\nすると、xがyのsubsetであることが必要\n一番上の桁を含むsubsetがx\n'


@lru_cache()
def F_naive(L, R):
    ret = 0
    ret += F((L + 1) // 2, (R + 1) // 2)
    answer = 0
    for x in range(L, R + 1):
        for y in range(x, R + 1):
            if x.bit_length() == y.bit_length() and (x ^ y) + x == y:
                answer += 1
    return answer


@lru_cache()
def F(L, R):
    if L < 0:
        L = 0
    if R < L:
        return 0
    if R == 0:
        return 0
    ret = 0
    ret += F((L + 1) // 2, R // 2)
    ret += F((L + 1) // 2, (R - 1) // 2)
    ret += G(L // 2, (R - 1) // 2)
    return ret


@lru_cache()
def G(L, R):
    if L < 0:
        L = 0
    if R < L:
        return 0
    if R == 0:
        return 1
    ret = 0
    ret += G((L + 1) // 2, R // 2)
    ret += F((L + 1) // 2, (R - 1) // 2)
    ret += G(L // 2, (R - 1) // 2)
    return ret


(L, R) = map(int, input().split())
answer = F(L, R) % MOD
print(answer)
