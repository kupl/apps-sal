from collections import Counter, deque
import itertools
import sys
import math
from math import gcd, pi, sqrt
INF = float("inf")

sys.setrecursionlimit(10**6)
def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    s = input()  # 暗号
    t = input()  # 含まれる文字

    s_len = len(s)
    t_len = len(t)
    flg = False

    for i in range(s_len - t_len, -1, -1):
        flg = True
        for j in range(t_len):
            if s[i + j] != t[j] and s[i + j] != "?":
                flg = False
                break
        if flg == True:
            trial = i
            break

    if flg == False:
        print("UNRESTORABLE")
        return

    ans = ""
    for i in s[:trial]:
        if i == "?":
            ans = ans + "a"
        else:
            ans = ans + i
    ans = ans + t

    for i in s[(trial + t_len):]:
        if i == "?":
            ans = ans + "a"
        else:
            ans = ans + i

    print(ans)


def __starting_point():
    main()


__starting_point()
