# E - Bullet

from collections import Counter
from math import gcd

n = int(input())
counter = Counter()  # 各ベクトルの個数
for i in range(n):
    a, b = list(map(int, input().split()))
    if b < 0:
        a, b = -a, -b  # 180度回転して第1〜2象限に
    elif b == 0:
        a = abs(a)
    if not a == b == 0:
        # 既約化
        g = gcd(a, b)
        a //= g
        b //= g
    counter[(a, b)] += 1

modulus = 1000000007

vs = set(counter)
# 第2象限のベクトルと直交するベクトルを追加
vs.update((b, -a) for a, b in counter if a <= 0)
# 第1象限のベクトルのみ抽出
vs = [(a, b) for a, b in vs if a > 0]

ncomb = 1  # イワシの選び方の個数
for a, b in vs:
    # 互いに仲が悪いイワシ群
    n1 = counter[(a, b)]
    n2 = counter[(-b, a)]
    # それぞれの群から好きな数だけイワシを選ぶ (0匹選ぶことも含む)
    m = pow(2, n1, modulus) + pow(2, n2, modulus) - 1
    ncomb = ncomb * m % modulus

ncomb -= 1  # 1匹も選ばない場合を除く

# (0, 0)のイワシを1匹だけ選ぶ
ncomb += counter[(0, 0)]

print((ncomb % modulus))
