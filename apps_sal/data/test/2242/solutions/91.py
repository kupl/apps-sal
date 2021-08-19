from itertools import accumulate
from collections import Counter


def solve(n):
    return n * (n - 1) // 2


s = input()[::-1]
MOD = 2019

# 事前計算
rest = []
for i, x in enumerate(s):
    # 1, 10, 100, 1000...の剰余を順に計算し、各桁までの剰余を計算
    if i == 0:
        tmp = 1
    else:
        tmp = tmp * 10 % MOD
    rest.append(int(x) * tmp % MOD)

result = [x % MOD for x in list(accumulate(rest))]

# 0は単独で2019の倍数
zero = result.count(0)

# 他はコンビネーションの結果
c = Counter(result)
c = list(c.values())

# 足して出力
print(sum([solve(x) for x in c if x >= 2]) + zero)
