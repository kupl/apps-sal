from decimal import ROUND_HALF_UP, Decimal  # 変換後の末尾桁を0や0.01で指定
from collections import deque, Counter, defaultdict  # すべてのkeyが用意されてる defaultdict(int)で初期化
from bisect import bisect_left as bileft, bisect_right as biright
from functools import lru_cache
from math import sqrt, ceil
import sys
mod = 10**9 + 7; inf = float("inf")
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
#Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
# 引数にlistはだめ
#######ここまでテンプレ#######
# ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########

n = int(input()); ans = -inf
F = []; P = []
for i in range(n):
    F.append(list(map(int, input().split())))
for i in range(n):
    P.append(list(map(int, input().split())))

for bit in range(1, 1 << 10):
    L = [(bit >> i) & 1 for i in range(10)]
    now = 0
    for i in range(n):
        cnt = 0
        for cc in range(10):
            if (F[i][cc] == 1 and L[cc] == 1): cnt += 1
        now += P[i][cnt]
    ans = max(ans, now)
print(ans)
