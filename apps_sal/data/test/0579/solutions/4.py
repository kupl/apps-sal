
import sys
from decimal import Decimal
import math
from itertools import combinations, product, accumulate
import bisect
from collections import Counter, deque, defaultdict

MOD = 10 ** 6 + 7
INF = 10 ** 9
PI = 3.14159265358979323846


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def lcm(a: int, b: int) -> int: return (a * b) // math.gcd(a, b)


def Main():
    n, k = read_ints()
    p = read_int_list()
    c = read_int_list()
    loop_list = []
    visit = [False] * n

    for i in range(n):
        if visit[i]:
            continue

        visit[i] = True
        now = i
        loop_tmp = []

        while True:
            now = p[now] - 1
            visit[now] = True
            loop_tmp.append(c[now])
            if visit[p[now] - 1]:
                loop_tmp.append(c[p[now] - 1])
                break
        loop_list.append(loop_tmp)

    ans = -10 ** 18

    for loop in loop_list:
        length = len(loop)
        score = sum(loop)
        if k > length:
            if score > 0:
                ans = max(ans, (k // length) * score + search_max_score(loop, k % length, length), (k // length - 1) * score + search_max_score(loop, length, length))
            else:
                ans = max(ans, search_max_score(loop, length, length))
        else:
            ans = max(ans, search_max_score(loop, k, length))

    print(ans)


def search_max_score(loop, rest, length):
    if rest == 0:
        ans = 0
    elif rest == 1:
        ans = max(loop)
    else:
        ans = -10**18
        loop += loop
        for i in range(length):
            tmp = list(accumulate(loop[i:i + rest]))
            ans = max(ans, max(tmp))

    return ans


if __name__ == '__main__':
    Main()
