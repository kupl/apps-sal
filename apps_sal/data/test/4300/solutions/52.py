import numpy as np
import itertools as itr

# 入力を受け取る
N = int(input())
D = list(map(int, input().split()))

# たこ焼きの全組み合わせを作成する
tako_cmb = np.array(list(itr.combinations(D,2)))

# (x,y)
# (x,y)
# (x,y)

# 全組み合わせの転置行列を作成して、味x,味yに分ける
xy = tako_cmb.T

# (x,x,x)
# (y,y,y)

# xとyの積の総和を求める
result = np.sum(xy[0]*xy[1])

# 結果を出力する
print(result)
