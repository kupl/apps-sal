# すぬけくんは 3匹のヤギにクッキーを渡したいです。
# すぬけくんは A枚のクッキーが入った缶と、
# B枚のクッキーが入った缶を持っています。
# すぬけくんは A, B, A + B のいずれかの枚数のクッキーを
# ヤギたちに渡すことができます。
# 3匹のヤギが同じ枚数ずつ食べられるように
# クッキーを渡すことが可能かどうか判定してください。

# 制約
# 1 ≦ A, B ≦ 100
# A, B はいずれも整数

# 標準入力から A, B を取得する
a, b = list(map(int, input().split()))


result = "ret"

# 以下、判定処理
if a % 3 == 0:  # Aの缶だけを渡して、3等分できる
    result = "Possible"
elif b % 3 == 0:  # Bの缶だけを渡して、3等分できる
    result = "Possible"
elif (a + b) % 3 == 0:  # A + B 缶を渡して、3等分できる
    result = "Possible"
else:
    result = "Impossible"

print(result)

