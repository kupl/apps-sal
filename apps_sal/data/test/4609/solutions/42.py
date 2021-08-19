from decimal import ROUND_HALF_UP, Decimal  # 変換後の末尾桁を0や0.01で指定
from collections import deque, Counter, defaultdict  # すべてのkeyが用意されてる defaultdict(int)で初期化
from bisect import bisect_left as bileft, bisect_right as biright
from functools import lru_cache
from math import sqrt, ceil
import sys
mod = 10**9 + 7
inf = float("inf")
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)
#Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
# 引数にlistはだめ
#######ここまでテンプレ#######
# ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########

n = int(input())
A = [int(input()) for i in range(n)]
C = Counter(A)
print(len([i for i in C.values() if i % 2 == 1]))
