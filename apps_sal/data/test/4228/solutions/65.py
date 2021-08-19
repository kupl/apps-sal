N, L = map(int, input().split())

# 元々の味（等差数列の和の公式より）
s = N * (2 * L + N - 1) // 2
# 味の絶対値が最小になるリンゴの味を求める
if L + N - 1 < 0:
    eat = L + N - 1
elif L > 0:
    eat = L
else:
    eat = 0

# 食べる（最適なリンゴ）以外の味の和
print(s - eat)
