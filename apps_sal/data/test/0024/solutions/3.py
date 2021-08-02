def check(r0, c0, dr, dc):
    cntx = 0
    cnte = 0
    for i in range(5):
        r = r0 + dr * i
        c = c0 + dc * i
        if r < 0 or 9 < r or c < 0 or 9 < c:
            break
        elif cells[r][c] == 'X':
            cntx += 1
        elif cells[r][c] == '.':
            cnte += 1
    return cntx == 4 and cnte == 1


cells = [list(input()) for _ in range(10)]
drc = [(1, 0), (0, 1), (1, 1), (1, -1)]
ans = 'NO'
for r0 in range(10):
    for c0 in range(10):
        for (dr, dc) in drc:
            if check(r0, c0, dr, dc):
                ans = 'YES'
print(ans)
