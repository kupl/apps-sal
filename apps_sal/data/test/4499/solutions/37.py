S = list(map(str, input().split()))

# 単語の先頭の文字をつなげ、大文字にした略語を出力してください

s1 = S[0][0].upper()
s2 = S[1][0].upper()
s3 = S[2][0].upper()

print(s1 + s2 + s3)
