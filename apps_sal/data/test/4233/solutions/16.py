def find_stars(h, w, matrix):
    max_size = 0
    if matrix[h][w] == '.':
        return max_size

    size = 1
    while True:
        for next_h in range(h, h + size + 1):
            if next_h >= height or matrix[next_h][w] != '*':
                return max_size
        for next_h in range(h, h - size - 1, -1):
            if next_h < 0 or matrix[next_h][w] != '*':
                return max_size
        for next_w in range(w, w + size + 1):
            if next_w >= width or matrix[h][next_w] != '*':
                return max_size
        for next_w in range(w, w - size - 1, -1):
            if next_w < 0 or matrix[h][next_w] != '*':
                return max_size

        max_size = size
        size += 1


height, width = list(map(int, input().split()))
matrix = []
for h in range(height):
    row = input()
    matrix.append(row)

result_matrix = [['.'] * width for h in range(height)]
result_stars = []
for h in range(height):
    for w in range(width):
        found_max_size = find_stars(h, w, matrix)
        if found_max_size == 0:
            continue

        for next_h in range(h, h + found_max_size + 1):
            result_matrix[next_h][w] = '*'
        for next_h in range(h, h - found_max_size - 1, -1):
            result_matrix[next_h][w] = '*'
        for next_w in range(w, w + found_max_size + 1):
            result_matrix[h][next_w] = '*'
        for next_w in range(w, w - found_max_size - 1, -1):
            result_matrix[h][next_w] = '*'

        result_stars.append(str(h + 1) + ' ' + str(w + 1) + ' ' + str(found_max_size))

is_equal = True
for h in range(height):
    for w in range(width):
        if matrix[h][w] != result_matrix[h][w]:
            is_equal = False

if is_equal:
    print(len(result_stars))
    for star in result_stars:
        print(star)
else:
    print(-1)

