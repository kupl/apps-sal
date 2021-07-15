c = input()

# 英小文字 c が与えられるので、cが母音であるか判定してください。
# c が母音であるとき、vowel と、そうでないとき consonant と出力せよ。

if c in ("a", "e", "i", "o", "u"):
    print("vowel")
else:
    print("consonant")
