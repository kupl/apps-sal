def solve(n, m, grid):
    n_free_cols = sum((all((grid[i][j] == 0 for i in range(n))) for j in range(m)))
    n_free_lines = sum((all((grid[i][j] == 0 for j in range(m))) for i in range(n)))
    N = min(n_free_lines, n_free_cols)
    return N % 2 == 1


def main():
    T = int(input())
    for _ in range(T):
        (n, m) = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(n)]
        print('Ashish' if solve(n, m, grid) else 'Vivek')


def __starting_point():
    main()


__starting_point()
