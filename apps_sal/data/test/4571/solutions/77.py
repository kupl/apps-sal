from decimal import Decimal  # floatの高精度ver, 渡すのはstr型で
from functools import lru_cache
from math import ceil
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
from collections import deque
from math import sqrt
import sys
import math
import heapq
mod = 10**9 + 7
inf = float("inf")
# すべてのkeyが用意されてる defaultdict(int)で初期化
# 順序を保ったdict
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
# 引数にlistはだめ
#######ここまでテンプレ#######
# ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########
n, m = list(map(int, input().split()))
A = 100 * (n - m) + 1900 * m
p = pow(2, m)


@lru_cache(maxsize=10**10)
def per(n):
    if n == 1:
        return 1 / p
    return (1 - sum([per(i) for i in range(1, n)])) * (1 / p)


ans = 0
for i in range(1, 2000):
    ans += i * A * per(i)
print((round(ans)))
