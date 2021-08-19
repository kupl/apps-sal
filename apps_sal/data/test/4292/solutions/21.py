#!/usr/bin/env python3
from collections import deque
import sys
sys.setrecursionlimit(1000000)

# スペース区切りの整数の入力
N, K = list(map(int, input().split()))
# 配列の入力
data = list(map(int, input().split()))

data.sort()

ans = 0
for i in range(K):
    ans += data[i]

print(ans)
