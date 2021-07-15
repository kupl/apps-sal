t = int(input())
for c in range(t):
    s = input()
    up_max = down_max = right_max = left_max = 0
    first_up = last_up = first_down = last_down = first_left = last_left = first_right = last_right = 0
    current_x = current_y = 0
    horizontal_count = vertical_count = 0
    for i in range(len(s)):
        if s[i] == 'W':
            current_y += 1
            vertical_count += 1
            if current_y > up_max:
                up_max = current_y
                first_up = last_up = i + 1
            elif current_y == up_max:
                last_up = i + 1
        elif s[i] == 'S':
            current_y -= 1
            vertical_count += 1
            if current_y < down_max:
                down_max = current_y
                first_down = last_down = i + 1
            elif current_y == down_max:
                last_down = i + 1
        elif s[i] == 'D':
            current_x += 1
            horizontal_count += 1
            if current_x > right_max:
                right_max = current_x
                first_right = last_right = i + 1
            elif current_x == right_max:
                last_right = i + 1
        else:
            current_x -= 1
            horizontal_count += 1
            if current_x < left_max:
                left_max = current_x
                first_left = last_left = i + 1
            elif current_x == left_max:
                last_left = i + 1

    h = up_max - down_max + 1
    w = right_max - left_max + 1
    ans = h * w
    if vertical_count > 1 and last_up < first_down:
        ans = min(ans, (h - 1) * w)
    if vertical_count > 1 and last_down < first_up:
        ans = min(ans, (h - 1) * w)
    if horizontal_count > 1 and last_right < first_left:
        ans = min(ans, h * (w - 1))
    if horizontal_count > 1 and last_left < first_right:
        ans = min(ans, h * (w - 1))

    print(ans)
