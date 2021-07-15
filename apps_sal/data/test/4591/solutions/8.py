a, b, c, x, y = map(int, input().split())

ans1 = x * a + y * b

min_xy = min(x, y)
ans2 = min_xy * 2 * c + (x - min_xy) * a + (y - min_xy) * b

max_xy = max(x, y)
ans3 = max_xy * 2 * c

print(min(ans1, ans2, ans3))
