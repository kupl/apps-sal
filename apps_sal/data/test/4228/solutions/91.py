N, L = map(int, input().split())

# 元々の味（等差数列の和の公式より）
s = N * (2 * L + N - 1) // 2
# 味の差の絶対値=リンゴiの味の絶対値
l = [abs(L + i) for i in range(N)]

# 味の絶対値が最小になるリンゴのindexを求め、sからその味を引けばよい
print(s - (L + l.index(min(l))))
