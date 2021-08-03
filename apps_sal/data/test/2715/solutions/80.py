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
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
# 引数にlistはだめ
#######ここまでテンプレ#######
# ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########
k = int(input())
print(50)
n = 50
if k == 0:
    print(" ".join(["0"] * 50))
    return

a = k // n
b = k % n
A = [a + 49 for i in range(50)]
for i in range(b):
    A = [A[j] - 1 if i != j else A[j] + n for j in range(50)]
print(*A)
