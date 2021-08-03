import math
from collections import deque
n, k = map(int, input().split())
v = list(map(int, input().split()))
# k回までだったー誤読
ans = 0
for i in range(1, min(k, n) + 1):
    # 取るところ(大きい方とは限らないのか)
    for m in range(i + 1):
        s = v[:m] + v[n - (i - m):]
        s.sort()
        # 取った個数より多く詰めようとしないように！
        # 残りk-i回ある
        for j in range(i, min(k, 2 * i)):  # それ以上詰められない場合
            # 0より小さい場合は書き換える
            if s[j - i] < 0:
                s[j - i] = 0
        # 取り出したやつの最大(戻す場合は0)
        ans = max(ans, sum(s))
        # 残りk-j回ある(breakの時のjはやってないので)
        # ここからはいい感じに出すのと入れるのを繰り返す(偶数の場合はこのままか)
        # 必要すらない、k回を使い切らなくていいので
        # print(sum(s))
print(ans)
