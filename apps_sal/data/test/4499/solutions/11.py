# 単語３つが空白区切りで与えられる
# 反語の先頭の文字をつなげる
# 大文字にする

a, b, c = map(str, input().split())

word = a[0] + b[0] + c[0]

print(word.upper())
