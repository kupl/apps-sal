# とりあえず解説を見ずに無理矢理解く。
# 全ての竹を「Aに使う・Bに使う・Cに使う・使わない」のどれかに振り分ける方法は
# 4**8 = 2**16 ≒ 64000なので全通り探索できる。
# C < B < Aなので、合成した後に長い順にすれば6分の1だけ調べれば良いが、該当の6分の1だけを抜き出すのは難しい
# どれかに使うが空集合になってるのは除外。

import itertools
n, a, b, c = list(map(int, input().split()))
nums = [int(input()) for _ in range(n)]

ans = 10**10

for usage_info in itertools.product(list(range(4)), repeat=n):

    mp = 0
    length = [0, 0, 0]
    for idx, usage in enumerate(usage_info):
        if usage == 3:
            continue
        if length[usage] > 0:
            mp += 10  # 合成魔法
        length[usage] += nums[idx]
    if min(length) == 0:
        continue

    mp += abs(length[0] - a) + abs(length[1] - b) + abs(length[2] - c)  # 延長、短縮魔法
    ans = min(ans, mp)

print(ans)

