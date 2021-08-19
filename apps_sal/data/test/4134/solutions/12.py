def go_up_to_down(w, h, value, steps):
    value ^= matrix[h][w]
    if steps == half_steps:
        if value not in counts[h][w]:
            counts[h][w][value] = 0
        counts[h][w][value] += 1
        return
    if w < width - 1:
        go_up_to_down(w + 1, h, value, steps + 1)
    if h < height - 1:
        go_up_to_down(w, h + 1, value, steps + 1)


def go_down_to_up(w, h, value, steps, count_ways):
    if steps == width + height - 2 - half_steps:
        if value ^ res_find in counts[h][w]:
            count_ways += counts[h][w][value ^ res_find]
        return count_ways
    delta = 0
    if w > 0:
        delta += go_down_to_up(w - 1, h, value ^ matrix[h][w], steps + 1, count_ways)
    if h > 0:
        delta += go_down_to_up(w, h - 1, value ^ matrix[h][w], steps + 1, count_ways)
    return count_ways + delta


(height, width, res_find) = [int(num) for num in input().split()]
matrix = []
for h in range(height):
    row = [int(num) for num in input().split()]
    matrix.append(row)
counts = [[dict()] * width for h in range(height)]
half_steps = (width + height - 2) // 2
go_up_to_down(0, 0, 0, 0)
count_ways = go_down_to_up(width - 1, height - 1, 0, 0, 0)
print(count_ways)
