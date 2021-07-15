import numpy as np

N = int(input())
A = list(map(int, input().split()))

# XOR和と加算和が等しくなるのは、二進数にしたときの各ビットの1の数が高々ひとつのとき
# → ある集合が条件を満たすとき、その部分集合も条件を満たす
# しゃくとり法
r = 0 # 右端の初期値
temp = 0
ans = 0 # 答えの初期値
for l in range(N): # 左端を動かしていく
    while r < N and temp ^ A[r] == temp + A[r]: # 右端を動かしても条件を満たすなら
        temp += A[r]
        r += 1
    # 条件を満たさなくなったら
    ans += r - l # 答えを更新
    # 左端を動かす準備
    if r == l:
        r += 1 # すでに重なっている場合は右端も動かす
        temp = 0
    else:
        temp -= A[l]
print(ans)
