# import logging


# fmt = r'%(levelname)s - %(name)s (line:%(lineno)s) - %(message)s'
# formatter = logging.Formatter(fmt)

# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# ch.setFormatter(formatter)

# logger = logging.getLogger()
# logger.setLevel(logging.ERROR)
# logger.addHandler(ch)


class StarCell:
    def __init__(self, row, col, top=None, bot=None, left=None, right=None):
        self.row = row
        self.col = col

        self.covered = False

        self.top = top
        self.bot = bot
        self.left = left
        self.right = right

        self._size = None
        self._size_top = None
        self._size_bot = None
        self._size_left = None
        self._size_right = None

    def set_adjacents(self, cells):
        row, col = self.row, self.col
        self.top = cells.get((row - 1, col), None)
        self.bot = cells.get((row + 1, col), None)
        self.left = cells.get((row, col - 1), None)
        self.right = cells.get((row, col + 1), None)

    def set_covered(self):
        size = self.size
        ctop = self
        cbot = self
        cleft = self
        cright = self
        for _ in range(size):
            ctop = ctop.top
            cbot = cbot.bot
            cleft = cleft.left
            cright = cright.right
            ctop.covered = True
            cbot.covered = True
            cleft.covered = True
            cright.covered = True

    @property
    def size_top(self):
        if not self.top:
            return 0
        if not self._size_top:
            # Update cache
            self._size_top = 1 + self.top.size_top
        return self._size_top

    @property
    def size_bot(self):
        if not self.bot:
            return 0
        if not self._size_bot:
            self._size_bot = 1 + self.bot.size_bot
        return self._size_bot

    @property
    def size_left(self):
        if not self.left:
            return 0
        if not self._size_left:
            self._size_left = 1 + self.left.size_left
        return self._size_left

    @property
    def size_right(self):
        if not self.right:
            return 0
        if not self._size_right:
            self._size_right = 1 + self.right.size_right
        return self._size_right

    @property
    def size(self):
        if not self._size:
            self._size = min(
                [self.size_top,
                 self.size_bot,
                 self.size_left,
                 self.size_right])
        return self._size

    def __repr__(self):
        if self.size > 0:
            return 'Star of max size {}'.format(self.size)
        return 'Cell covered? {}'.format(self.covered)


def solve(grid):
    n, m = len(grid), len(grid[0])

    cells = {}
    for row in range(n):
        for col in range(m):
            if grid[row][col] == '.':
                continue
            cells[(row, col)] = StarCell(row, col)

    for key, val in list(cells.items()):
        val.set_adjacents(cells)

    for key, val in list(cells.items()):
        val.set_covered()

    # for key, val in cells.items():
    #     print(key, val)

    ans = []
    for key, val in list(cells.items()):
        if val.size == 0 and not val.covered:
            return None
        if val.size > 0:
            ans.append([val.row + 1, val.col + 1, val.size])  # Rebase index 1
    return ans


def main():
    n, m = list(map(int, input().strip().split()))
    grid = [list(input().strip()) for _ in range(n)]

    results = solve(grid)
    if results is None:
        print('-1')
    else:
        print(len(results))
        for result in results:
            print(*result)


def __starting_point():
    main()


__starting_point()
