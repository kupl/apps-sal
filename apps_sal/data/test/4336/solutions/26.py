W, H, x, y = map(int, input().split())
ans1, ans2 = W * H / 2, 0
if 2 * x == W and 2 * y == H:
    ans2 = 1
print(ans1, ans2)
