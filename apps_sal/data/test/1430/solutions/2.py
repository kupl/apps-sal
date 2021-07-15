"""
keyword: 尺取法
"""

import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
s = input()

nums = []
now = 1 # 今見ている数
cnt = 0 # nowがいくつ並んでいるか

for i in range(n):
    if s[i] == str(now):
        cnt += 1
    else:
        nums.append(cnt)
        now ^= 1 # 0と1を切り替える
        cnt = 1 # 新しいのをカウント
if cnt != 0:
    nums.append(cnt)

# 1-0-1-0-1-0-1って感じの配列が欲しい
# 1-0-1-0みたいに0で終わっていたら、適当に1つ足す
# 補足：1-0-1-0-1というのは、1が0個、0が2個、1が1個、、、などと並んでいるという意味。このとき1つ目の0をひっくり返すと1-1-1と連続する。1-...-1と連続している数が求める値なので、左端と右端は1にしたい
if len(nums)%2 == 0:
    nums.append(0)
    
add = 2*k+1

ans = 0
left = 0
right = 0
tmp = 0 # [left, right)のsum

# 1-0-1...の、1から始まり1で終わる範囲を見るので、偶数番目だけ見る
for i in range(0, len(nums), 2):
    
    nextleft = i
    nextright = min(i+add, len(nums))
    
    # 左端を移動
    while (nextleft > left):
        tmp -= nums[left]
        left += 1
    # 右端を移動
    while (nextright > right):
        tmp += nums[right]
        right += 1
        
    ans = max(tmp, ans)
    
print(ans)
