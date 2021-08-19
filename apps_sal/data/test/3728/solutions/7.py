(n, m) = map(int, input().split())
iden = list(range(1, m + 1))
b = [[int(x) for x in input().split()] for _ in range(n)]


def run(board):
    okay = True
    for row in board:
        s = 0
        for (x, y) in zip(row, iden):
            s += x != y
        okay = okay and s in {0, 2}
    return okay


okay = run(b)
for i in range(m):
    for j in range(m):
        if i == j:
            continue
        B = [row[:] for row in b]
        for k in range(n):
            (B[k][i], B[k][j]) = (B[k][j], B[k][i])
        okay = okay or run(B)
print('YES' if okay else 'NO')
