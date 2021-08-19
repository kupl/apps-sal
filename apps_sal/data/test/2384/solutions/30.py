# 写経AC
from collections import defaultdict

N = int(input())
A = [int(i) for i in input().split()]

# dp[(i, x, flag)]:= i番目まででx個選んでいる時の最大値
# flag: i番目をとるフラグ
dp = defaultdict(lambda: -float("inf"))

# 初期条件
dp[(0, 0, 0)] = 0

for i, a in enumerate(A, 1):
    for x in range((i // 2) - 1, (i + 1) // 2 + 1):
        dp[(i, x, 0)] = max(dp[(i - 1, x, 0)], dp[(i - 1, x, 1)])
        dp[(i, x, 1)] = dp[(i - 1, x - 1, 0)] + a

print(max(dp[(N, N // 2, 0)], dp[(N, N // 2, 1)]))
