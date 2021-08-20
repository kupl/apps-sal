(rows, cols, r, c) = map(int, input().split())
s = input()
r -= 1
c -= 1
field = [[0] * cols for i in range(rows)]
res = [0] * len(s)
field[r][c] = 1
cnt = 1
for i in range(len(s)):
    if s[i] == 'U':
        if r > 0:
            r -= 1
    elif s[i] == 'R':
        if c < cols - 1:
            c += 1
    elif s[i] == 'D':
        if r < rows - 1:
            r += 1
    elif s[i] == 'L':
        if c > 0:
            c -= 1
    if field[r][c] == 0:
        res[i] = 1
        cnt += 1
        field[r][c] = 1
res[len(s) - 1] += rows * cols - cnt
print(1, ' '.join(map(str, res)))
