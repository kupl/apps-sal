import sys as _sys


def main():
    t = int(input())
    for i_t in range(t):
        (rows_n, columns_n) = _read_ints()
        rows = [tuple(_read_ints()) for i_row in range(rows_n)]
        columns = [tuple(_read_ints()) for i_column in range(columns_n)]
        any_first_column_element = rows[0][0]
        i_first_column = 0
        while any_first_column_element not in columns[i_first_column]:
            i_first_column += 1
        first_column = columns[i_first_column]
        rows = sorted(rows, key=lambda row: first_column.index(row[0]))
        for row in rows:
            print(*row)


def _read_line():
    result = _sys.stdin.readline()
    assert result[-1] == '\n'
    return result[:-1]


def _read_ints():
    return list(map(int, _read_line().split()))


def __starting_point():
    main()


__starting_point()
