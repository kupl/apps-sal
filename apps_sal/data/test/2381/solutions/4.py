from bisect import bisect_left, bisect_right  # 二分探索
from heapq import heapify, heappush, heappop, heappushpop  # プライオリティキュー
from collections import defaultdict  # 初期化済み辞書
from collections import deque  # 双方向キュー
import sys
def s2nn(s): return [int(c) for c in s.split(' ')]
def ss2nn(ss): return [int(s) for s in ss]
def ss2nnn(ss): return [s2nn(s) for s in ss]
def i2s(): return sys.stdin.readline().rstrip()
def i2n(): return int(i2s())
def i2nn(): return s2nn(i2s())
def ii2ss(n): return [sys.stdin.readline().rstrip() for _ in range(n)]
def ii2sss(n): return [list(sys.stdin.readline().rstrip()) for _ in range(n)]
def ii2nn(n): return ss2nn(ii2ss(n))
def ii2nnn(n): return ss2nnn(ii2ss(n))


sys.setrecursionlimit(int(1e+6))
MOD = int(1e+9) + 7
# import numpy as np  # 1.8.2
# import scipy  # 0.13.3


def main():
    N, K = i2nn()
    A = i2nn()
    # 選択の余地がない場合、全部掛けるしかない
    if N == K:
        n = 1
        for a in A:
            n = (n * a) % MOD
        print(n)
        return

    Ap = [n for n in A if n >= 0]
    An = [-n for n in A if n < 0]
    Ap.sort()
    Ap.reverse()
    An.sort()
    An.reverse()
    Np = len(Ap)
    Nn = len(An)
    # 結果はプラスにしたい。Aiが全部マイナスかつKが奇数だとNG
    # 結果をプラスにできない場合、絶対値を最小化する
    if N == Nn and K % 2 == 1:
        n = 1
        A.sort()
        A.reverse()
        for i in range(K):
            n = (n * A[i]) % MOD
        print(n)
        return

    n = 1
    k = K
    i = 0
    j = 0
    # 結果をプラスに場合、プラスを維持しつつ、絶対値を最大化する
    # Kは偶数で考えたい。Kが奇数のとき、一番大きな正の数を取る
    if k % 2 == 1:
        n = (n * Ap[i]) % MOD
        i += 1
        k -= 1
    while k > 0:
        if Np - i < 2:
            n = (n * An[j]) % MOD
            j += 1
            n = (n * An[j]) % MOD
            j += 1
        elif Nn - j < 2:
            n = (n * Ap[i]) % MOD
            i += 1
            n = (n * Ap[i]) % MOD
            i += 1
        else:
            np = Ap[i] * Ap[i + 1]
            nn = An[j] * An[j + 1]
            if np >= nn:
                n = (n * np) % MOD
                i += 2
            else:
                n = (n * nn) % MOD
                j += 2
        k -= 2
    print(n)


main()
