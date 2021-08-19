a, b, x, y = [int(hoge) for hoge in input().split()]
# 階段 y分
# ろうか x分
stair = min(y, 2 * x)
isle = x
ans = 0
if a > b:
    # くだり
    # Aのb+1階に行く + x分
    ans = (a - b - 1) * stair + isle
else:
    # のぼり
    # 真横に行って階段で登るしか無い
    ans = (b - a) * stair + isle
print(ans)
