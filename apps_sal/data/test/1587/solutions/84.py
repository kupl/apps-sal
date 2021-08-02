
# 初期入力
from bisect import bisect_left
import sys
# input = sys.stdin.readline  #文字列では使わない
N = int(input())
c = input().strip()
ans = 0
r = [i for i, x in enumerate(c) if x == 'R']  # 全体の中でRのIndex
r_num = len(r)  # 全体でRの数

ans = bisect_left(r, r_num)  # 呪われないためのRとWの境界
print(r_num - ans)  # 境界より右側のRの数
