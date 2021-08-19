def lmap(func, x): return list(map(func, x))


_, scobes = input(), input()  # '', '[[[][][][][][][][]][]][]'
scobes = scobes.replace('[]', '[   ]')


def empty_list(s):
    return [0] * s


def two_dim_array(size):
    return [empty_list(size[0]) for i in range(size[1])]


def process_scobes(scobes):

    depthes = []
    depth = 0
    for i, scobe in enumerate(scobes):
        if scobe == '[':
            depth += 1
        depthes.append(depth)

        if scobe == ']':
            depth -= 1

    max_depth = max(depthes)
    depthes = lmap(lambda val: 2 * (max_depth - val + 1) + 1, depthes)
    return depthes


def set_on_interval(from_, to_):
    pass


def draw_scobes_into_array(scobes, heights):
    picture = two_dim_array([len(scobes), max(heights)])
    middle = (max(heights) + 1) // 2

    for i, scobe in enumerate(scobes):
        h = heights[i] // 2 - 1
        if scobe != ' ':
            for height in range(middle - h - 1, middle + h):
                picture[height][i] = 1

            picture[middle - h - 2][i] = 2
            picture[middle + h][i] = 2
            offset = 1 if scobe == '[' else -1
            picture[middle - h - 2][i + offset] = 3
            picture[middle + h][i + offset] = 3

    return picture


heights = process_scobes(scobes)

picture = draw_scobes_into_array(scobes, heights)


def draw_line(line): return ''.join(lmap(str, line)).replace('0', ' ').replace('1', '|').replace('2', '+').replace('3', '-')


print('\n'.join(lmap(draw_line, picture)))

# Here was me!
