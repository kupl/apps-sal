w, h, x, y = map(int, input().split())
# 面積が大きくない方の最大値
s = 0.5 * w * h
# 複数存在するかの判定
i = 0
if 2 * x == w and 2 * y == h:
    i += 1
print(s, i)
