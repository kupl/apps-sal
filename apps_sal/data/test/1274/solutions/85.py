from math import factorial as fact
import math
import sys
from itertools import product
import numpy as np
from collections import Counter
import datetime
from collections import deque
from bisect import bisect_left, bisect_right
import heapq


# 入力:N(int:整数)
def input1():
    return int(input())

# 入力:N,M(int:整数)


def input2():
    return list(map(int, input().split()))

# 入力:[n1,n2,...nk](int:整数配列)


def input_array():
    return list(map(int, input().split()))


n, m = input2()
AB = [[] for _ in range(m)]


for i in range(n):
    a, b = input2()
    if a - 1 < m:  # 報酬受取日がmを超える仕事は除外する
        AB[a - 1].append(-b)  # heapqの仕様のため，-を追加

ans = 0
heap = []
for i in range(m):
    for b in AB[i]:
        heapq.heappush(heap, b)
    # 最大値をheapから取り出し
    if len(heap) > 0:
        MAX = heapq.heappop(heap)
        ans += -MAX
print(ans)
