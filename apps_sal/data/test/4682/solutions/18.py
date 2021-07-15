# 045_a
a = int(input())  # 上底の長さ
b = int(input())  # 下底の長さ
h = int(input())  # 高さ

if (1 <= a & a <= 100) & (1 <= b & b <= 100) & (1 <= h & h <= 100):
    if (h % 2 == 0):
        s = int((a + b) * h / 2)
        print(s)
