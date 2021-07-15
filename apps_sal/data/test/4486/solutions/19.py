# abc072B
# https://atcoder.jp/contests/abc072/tasks/abc072_b

# 英小文字からなる文字列 s
# 前から奇数文字目だけを抜き出し文字列を出力
# 先頭の文字を１文字目とする


# 入力
s = str(input())

# 処理
# 奇数番目文字の抜き出し
print((s[::2]))

