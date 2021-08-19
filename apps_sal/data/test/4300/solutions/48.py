from itertools import combinations as cmb
import numpy as np

# たこ焼きの個数Nを取得
N = int(input())

# 各たこ焼きの味を取得
d = list(map(int, input().split()))

# たこ焼きの全組み合わせを作り、xとyに分離させる
x, y = np.array(list(cmb(d, 2))).T

# 体力の回復量の総和を求めて表示
print(np.sum(x * y))
