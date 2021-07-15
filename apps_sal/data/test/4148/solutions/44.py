import numpy as np

# 文字列Sのシフト数Nを取得
N = int(input())

# 文字列Sを取得
S = input()

# 文字列Sの各文字をasciiに変換
ascii_S = np.array(list(map(ord, S))) - 65

# asciiの数値をN分シフトさせる
shift_ascii_S = list(map(lambda x: 65 + np.mod(x + N, 26), ascii_S))

# ascii変換をそれぞれ文字に逆変換して結合
shift_S = ''.join(list(map(chr, shift_ascii_S)))

# 結果出力
print(shift_S)
