from collections import Counter


def main():
    H, W, M = list(map(int, input().split()))
    bombs = [list(map(int, input().split())) for _ in range(M)]
    counter_row = Counter([h for h, _ in bombs])
    val_max_row, max_rows = 0, []
    for h, v in counter_row.items():
        if val_max_row < v:
            val_max_row = v
            max_rows = [h]
        elif val_max_row == v:
            max_rows.append(h)
    counter_col = Counter([w for _, w in bombs])
    val_max_col, max_cols = 0, []
    for w, v in counter_col.items():
        if val_max_col < v:
            val_max_col = v
            max_cols = [w]
        elif val_max_col == v:
            max_cols.append(w)
    # 基本的には val_max_row + val_max_col が答え。
    # 行・列で重複カウントになるケースだった場合はここから1引かないといけない。
    max_rows = Counter(max_rows)
    max_cols = Counter(max_cols)
    n_max_cells = len(max_rows.keys()) * len(max_cols.keys())
    n_cells = 0
    for h, w in bombs:
        if max_rows[h] > 0 and max_cols[w] > 0:
            n_cells += 1
    ans = val_max_row + val_max_col
    if n_cells >= n_max_cells:
        ans -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
