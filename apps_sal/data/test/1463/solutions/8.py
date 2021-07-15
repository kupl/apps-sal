def check(r, c, x):
    rtn = False
    rs = [a[r][i] for i in range(n) if i != c]
    cs = [a[i][c] for i in range(n) if i != r]
    for r in rs:
        for c in cs:
            if r + c == x:
                rtn = True
                break
    return rtn

n = int(input())
a = [list(map(int, input().split()))for _ in range(n)]

ans = True
for i in range(n):
    for j in range(n):
        if a[i][j] != 1:
            ans &= check(i, j, a[i][j])

print('Yes' if ans else 'No')

