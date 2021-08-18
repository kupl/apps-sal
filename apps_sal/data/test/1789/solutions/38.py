a, b, x, y = [int(hoge) for hoge in input().split()]
stair = min(y, 2 * x)
isle = x
ans = 0
if a > b:
    ans = (a - b - 1) * stair + isle
else:
    ans = (b - a) * stair + isle
print(ans)
