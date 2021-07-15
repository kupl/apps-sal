N, D = map(int, input().split())
# 一人の監視員は2D + 1本の木を監視できる
# N//(2D + 1) と 余りがあれば1を足した人数が必要になる
import math
print(int(math.ceil(N / (2*D + 1))))
