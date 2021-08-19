# 文字を取得
c = str(input())
v_list = ["a", "e", "i", "o", "u"]

# 母音なのかを確認し結果を出力
if c in v_list:
    print("vowel")
else:
    print("consonant")
