# 和、徐、積の中で最大値を出力する

A, B = list(map(int, input().split()))

lists = [A + B, A - B, A * B]

print((max(lists)))
