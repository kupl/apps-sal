# 最小の移動距離は、一番端から反対側まで一直線に移動する事。
# 行ったり来たりする可能性はない
n = int(input())
a = list(map(int, input().split()))
# 座標は正の整数のみなのでmax-minで計算できそう。
# print(mix-min)
print(max(a) - min(a))
