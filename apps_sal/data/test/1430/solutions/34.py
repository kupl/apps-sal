"""
keyword: 累積和
"""

import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
s = input()

nums = []
now = 1  # 今見ている数
cnt = 0  # nowがいくつ並んでいるか

for i in range(n):
    if s[i] == str(now):
        cnt += 1
    else:
        nums.append(cnt)
        now ^= 1  # 0と1を切り替える
        cnt = 1  # 新しいのをカウント
if cnt != 0:
    nums.append(cnt)

# 1-0-1-0-1-0-1って感じの配列が欲しい
# 1-0-1-0みたいに0で終わっていたら、適当に1つ足す
# 補足：1-0-1-0-1というのは、1が0個、0が2個、1が1個、、、などと並んでいるという意味。このとき1つ目の0をひっくり返すと1-1-1と連続する。1-...-1と連続している数が求める値なので、左端と右端は1にしたい
if len(nums) % 2 == 0:
    nums.append(0)

add = 2 * k + 1

# 累積和を作る
tot = [0] * (len(nums) + 1)
for i in range(len(nums)):
    tot[i + 1] = tot[i] + nums[i]

ans = 0

# 1-0-1...の、1から始まり1で終わる範囲を見るので、偶数番目だけ見る
for i in range(0, len(nums), 2):

    # 次のleft, rightを計算する
    left = i
    right = min(i + add, len(nums))
    tmp = tot[right] - tot[left]

    ans = max(tmp, ans)

print(ans)
