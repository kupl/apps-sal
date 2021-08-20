def solution(heights, n, m):
    rows = []
    cols = []
    for j in range(n):
        lst = set()
        for i in range(m):
            lst.add(heights[j][i])
        rows.append({x: i for (i, x) in enumerate(sorted(lst))})
    for i in range(m):
        lst = set()
        for j in range(n):
            lst.add(heights[j][i])
        cols.append({x: i for (i, x) in enumerate(sorted(lst))})
    for j in range(n):
        answer = []
        for i in range(m):
            val = heights[j][i]
            rank_row = rows[j][val]
            rank_col = cols[i][val]
            value = max(rank_row, rank_col) + max(len(rows[j]) - rank_row, len(cols[i]) - rank_col)
            answer.append(str(value))
        print(' '.join(answer))


def get():
    (n, m) = list(map(int, input().split()))
    data = []
    for j in range(n):
        data.append(list(map(int, input().split())))
    solution(data, n, m)


get()
