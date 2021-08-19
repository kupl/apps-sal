K, X = map(int, input().split())

# K個の黒い石、X座標にある石は黒い
# 黒で塗られている石が置かれている可能性のある座標をすべて、空白で区切って小さい順に出力せよ

black_stone = []

for i in range(X - K + 1, X + K):
    black_stone.append(i)

black_stone = [str(a) for a in black_stone]
black_stone = " ".join(black_stone)
print(black_stone)
