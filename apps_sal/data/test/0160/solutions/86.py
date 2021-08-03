import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


def make_divisors(n):  # nの約数を列挙
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort(reverse=True)
    return divisors


# 全ての合計の約数が答えの候補、上から可能かどうか見ていく
N, K = lr()
A = np.array(lr())
total = A.sum()
D = make_divisors(total)  # 降順
for d in D:
    B = A % d
    B.sort()
    inc = d - B
    B_cum = B.cumsum()
    inc_cum = inc.cumsum()
    for i in range(N):
        x = B_cum[i]
        y = inc_cum[N - 1] - inc_cum[i]
        if x > K:  # xは単調増加
            break
        if y > K:
            continue
        if (x + y) // 2 <= K:
            print(d)
            return
