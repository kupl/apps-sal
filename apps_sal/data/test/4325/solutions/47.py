import math

N, X, T = map(int, input().split())
# N 作るたこ焼きの個数
# X 一度に作れるたこ焼きの個数
# T かかる時間

t_times = N / X

result = T * math.ceil(t_times)

print(result)
