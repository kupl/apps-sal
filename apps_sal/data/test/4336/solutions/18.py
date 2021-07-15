W, H, x, y = map(int, input().split())
ans1 = W*H/2
ans2 = 1 if W/2 == x and H/2 == y else 0
print(ans1, ans2)
