"""Codeforces Round #419 (Div. 1) - Karen and Game.

http://codeforces.com/contest/815/problem/A

On the way to school, Karen became fixated on the puzzle game on her phone!

The game is played as follows. In each level, you have a grid with n rows and
m columns. Each cell originally contains the number 0.

One move consists of choosing one row or column, and adding 1 to all of the
cells in that row or column.

To win the level, after all the moves, the number in the cell at the i-th row
and j-th column should be equal to gi, j.

Karen is stuck on one level, and wants to know a way to beat this level using
the minimum number of moves. Please, help her with this task!

Input:

The first line of input contains two integers, n and m (1 ≤ n, m ≤ 100), the
number of rows and the number of columns in the grid, respectively.

The next n lines each contain m integers. In particular, the j-th integer in
the i-th of these rows contains gi, j (0 ≤ gi, j ≤ 500).

Output:

If there is an error and it is actually not possible to beat the level, output
a single integer -1.

Otherwise, on the first line, output a single integer k, the minimum number of
moves necessary to beat the level.

The next k lines should each contain one of the following, describing the
moves in the order they must be done:

- row x, (1 ≤ x ≤ n) describing a move of the form "choose the x-th row".

- col x, (1 ≤ x ≤ m) describing a move of the form "choose the x-th column".

If there are multiple optimal solutions, output any one of them.

"""
import logging

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logger.addHandler(ch)


def solve(n, m, grid):
    logger.debug('\n'.join([str(x) for x in grid]))

    # Check if ...
    a = [grid[i][0] for i in range(n)]
    b = [grid[0][i] - grid[0][0] for i in range(m)]
    if any(grid[i][j] != a[i] + b[j] for i in range(n) for j in range(m)):
        logger.debug('Not possible ....')
        return [-1]

    best_move, best = None, float('inf')
    for z in range(501):
        a = [grid[i][0] - z for i in range(n)]
        b = [z + grid[0][i] - grid[0][0] for i in range(m)]
        logger.debug('z = %s', z)
        logger.debug('a = %s', a)
        logger.debug('b = %s', b)
        if any(x < 0 for x in a + b):
            logger.debug('Non-positives on z %s', z)
            continue
        current = sum(a) + sum(b)
        if current < best:
            best_move = z
            best = current

    if best_move is None:
        return [-1]

    logger.debug('Best move is %s', best_move)

    res = []
    res.append(best)

    a = [grid[i][0] - best_move for i in range(n)]
    for i, times in enumerate(a):
        if not times:
            continue
        res.extend(['row {}'.format(i + 1)] * times)

    b = [best_move + grid[0][i] - grid[0][0] for i in range(m)]
    for i, times in enumerate(b):
        if not times:
            continue
        res.extend(['col {}'.format(i + 1)] * times)

    return res


def main():
    n, m = list(map(int, input().strip().split()))
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    result = solve(n, m, grid)
    print('\n'.join(map(str, result)))


def __starting_point():
    main()

__starting_point()
