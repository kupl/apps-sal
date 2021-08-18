
"""

https://atcoder.jp/contests/arc106/tasks/arc106_f

シンプルに解けるはず
穴が足りない場合は0

====答えを見た====

各部品で特別な穴を選ぶ (Πd通り)
そうでない穴に関して自分と連結でない奴とくっつける

毎回、普通の穴を1つ選び、そこに部品を一つ選んで特別な穴とくっつける
→最後の穴が邪魔
→特別な穴が2個になったらそれをくっつける

すると、矢印が最後に接続した場所に向いた木になる
出来上がる木は、

(S-N)*(N-1) * (S-N-1)*(N-2) * … * (S-N-(N-3))*(N-(N-2))

被って数えているのは
(N-1)!通り
なので、

(S-N)*(S-N-1)*…*(S-N-(N-3))
通り

"""

import sys
from sys import stdin

N = int(stdin.readline())
d = list(map(int, stdin.readline().split()))
S = sum(d)

if sum(d) < 2 * (N - 1):
    print((0))
    return

mod = 998244353
ans = 1
for i in d:
    ans *= i
    ans %= mod

for i in range(S - N, S - 2 * N + 3 - 1, -1):
    ans *= i
    ans %= mod
print(ans)
