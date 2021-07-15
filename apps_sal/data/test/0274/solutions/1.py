class Screen:
    def __init__(self, n_rows):
        self.rows = [[] for _ in range(n_rows)]
        self.height = n_rows

    def draw(self, x, y, c):
        row = self.rows[y]
        while x > len(row) - 1:
            row.append(' ')
        row[x] = c

    def draw_open(self, x, height):
        middle = self.height // 2
        self.draw(x, middle, '|')
        for dy in range(1, height + 1):
            self.draw(x, middle + dy, '|')
            self.draw(x, middle - dy, '|')
        self.draw(x, middle + height + 1, '+')
        self.draw(x + 1, middle + height + 1, '-')
        self.draw(x, middle - height - 1, '+')
        self.draw(x + 1, middle - height - 1, '-')

    def draw_close(self, x, height):
        middle = self.height // 2
        self.draw(x, middle, '|')
        for dy in range(1, height + 1):
            self.draw(x, middle + dy, '|')
            self.draw(x, middle - dy, '|')
        self.draw(x, middle + height + 1, '+')
        self.draw(x - 1, middle + height + 1, '-')
        self.draw(x, middle - height - 1, '+')
        self.draw(x - 1, middle - height - 1, '-')

    def strings(self):
        return [''.join(row) for row in self.rows]


def to_heights(seq):
    depths = []
    cur_depth = 0
    for par in seq:
        if par == '[':
            depths.append(cur_depth)
            cur_depth += 1
        else:
            cur_depth -= 1
            depths.append(cur_depth)
    max_depth = max(depths)
    heights = [max_depth - depth for depth in depths]
    return heights


def to_strings(seq, heights):
    n_rows = 2 * (max(heights) + 1) + 1
    screen = Screen(n_rows)
    cur_x = 0
    prev_par = None
    for par, height in zip(seq, heights):
        if par == '[':
            screen.draw_open(cur_x, height)
            cur_x += 1
        if par == ']':
            if prev_par == '[':
                cur_x += 3
            screen.draw_close(cur_x, height)
            cur_x += 1
        prev_par = par
    return screen.strings()





n = int(input())
seq = input()
heights = to_heights(seq)
strings = to_strings(seq, heights)
for string in strings:
    print(string)


