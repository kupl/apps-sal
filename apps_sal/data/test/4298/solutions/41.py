import math
N, D = map(int, input().split())
 
# 前から最適に配置せよ
# 一人目は, 1,...,D, D+1, D+2,...,2D+1 を監視
# 二人目は, 2D+2,..., 3D+2, ...,4D+2 を監視
# x人まで繰り返すと、1,...,x(2D+1)まで監視できる
 
# x(2D+1) > N を満たす最小のxは？
# x_min = ceil(N/(2D+1))
 
print(math.ceil(N/(2*D+1)))
