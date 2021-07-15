# 初期入力
from bisect import bisect_left
import sys
#input = sys.stdin.readline  #文字列では使わない
N = int(input())
c =input().strip()
ans =0
w =[i for i, x in enumerate(c) if x == 'W']
r =[i for i, x in enumerate(c) if x == 'R']
w_num =len(w) #全体でWの数
r_num =len(r) #全体でRの数

ans =bisect_left(r,r_num)
print(r_num -ans)
