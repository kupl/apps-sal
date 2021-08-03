tc_count = int(input())

ans = []

for i in range(tc_count):
    size = list(map(int, input().split()))
    w = size[1]
    h = size[0]
    white = list(map(int, input().split()))
    black = list(map(int, input().split()))
    black_count = (w * h) // 2
    white_count = (w * h) - black_count

    white_area = (white[3] - white[1] + 1) * (white[2] - white[0] + 1)
    if (white[0] + white[1]) % 2 == 0:
        become_white = (white_area // 2)
    else:
        become_white = white_area - (white_area // 2)
    black_count = black_count - become_white
    white_count = white_count + become_white

    black_area = (black[3] - black[1] + 1) * (black[2] - black[0] + 1)
    if (black[0] + black[1]) % 2 == 0:
        become_black = black_area - (black_area // 2)
    else:
        become_black = black_area // 2
    white_count = white_count - become_black
    black_count = black_count + become_black

    left_x = max(black[0], white[0])
    left_y = max(black[1], white[1])
    right_x = min(black[2], white[2])
    right_y = min(black[3], white[3])
    orig_b = 0
    if left_x <= right_x and left_y <= right_y:
        rect_count = (right_x - left_x + 1) * (right_y - left_y + 1)
        orig_b = rect_count // 2 if (left_x + left_y) % 2 == 0 else rect_count - (rect_count // 2)
    white_count = white_count - orig_b
    black_count = black_count + orig_b
    ans.append(str(white_count) + " " + str(black_count))

for an in ans:
    print(an)
