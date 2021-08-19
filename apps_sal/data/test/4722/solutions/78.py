# A - Sharing Cookies

# 3匹のヤギにクッキーを渡したい
# A 枚入ったクッキーが入った缶
# B 枚入ったクッキーが入った缶
# A B 缶を持っている。

#  A, B, A + B のいずれかの枚数をヤギに渡すことができる

# 3匹のヤギが同じ枚数食べれるように渡せるか判定する
# 可能なら Possible    不可能なら Impossible

# A B を標準入力で取得
A, B = list(map(int, input().split()))
# print(A, B)

# A の場合 Bの場合 A + B の場合で分ける
# それぞれの余りが 0 の時 Possible
# それ以外は Impossible

if A % 3 == 0:
    answer = "Possible"
elif B % 3 == 0:
    answer = "Possible"
elif (A + B) % 3 == 0:
    answer = "Possible"
else:
    answer = "Impossible"

# 結果を出力
print(answer)
