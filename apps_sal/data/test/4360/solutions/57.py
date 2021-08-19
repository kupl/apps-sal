# 入力から逆数の総和を取りその逆数を出力する
input()
print(1 / sum(map(lambda x: 1 / int(x), input().split())))
