import sys
mod=10**9+7 ; inf=float("inf")
from math import sqrt, ceil
from collections import deque, Counter, defaultdict #すべてのkeyが用意されてる defaultdict(int)で初期化
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
from bisect import bisect_left as bileft, bisect_right as biright
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########
n,m=list(map(int,input().split()))
A=[int(input()) for i in range(m)]
NG=[0]*(10**5+10)
for i in A:
    NG[i]=1


@lru_cache(maxsize=10**10)
def qwe(x):
    if x==n:return 1
    if x>n:return 0
    if NG[x+1] and NG[x+2]: print((0));return
    if NG[x+1]:return qwe(x+2)%mod
    if NG[x+2]:return qwe(x+1)%mod
    return (qwe(x+2)+qwe(x+1))%mod
print((qwe(0)))
    

