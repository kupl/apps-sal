(h, w) = list(map(int, input().split()))
ans = 10 ** 9
if h % 3 == 0 or w % 3 == 0:
    ans = 0
else:
    for width in range(1, w):
        left = width * h
        if h % 2 == 0:
            right_up = (w - width) * (h // 2)
            right_down = right_up
        else:
            right_up = (w - width) * (h // 2 + 1)
            right_down = (w - width) * (h // 2)
        ans = min(ans, max(left, right_up, right_down) - min(left, right_up, right_down))
    for height in range(1, h):
        up = w * height
        if w % 2 == 0:
            down_left = w // 2 * (h - height)
            down_right = down_left
        else:
            down_left = w // 2 * (h - height)
            down_right = (w // 2 + 1) * (h - height)
        ans = min(ans, max(up, down_left, down_right) - min(up, down_left, down_right))
    ans = min(ans, min(h, w))
print(ans)
