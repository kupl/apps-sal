import numpy as np

# 文字列Sのシフト数Nを取得
N = int(input())

# 文字列Sを取得
S = input()

# Aのascii
base_ascii = 65

# アルファベットリスト
als = [chr(a) for a in range(65, 90 + 1)]

# 文字列Sの各文字をasciiに変換
ascii_S = np.array(list(map(ord, S))) - base_ascii

print(''.join([als[np.mod(s + N, len(als))] for s in ascii_S]))
