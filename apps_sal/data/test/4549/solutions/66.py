(h, w) = map(int, input().split())
c = [input() for _ in range(h)]
ans = 'Yes'
for i in range(h):
    for j in range(w):
        if c[i][j] == '#':
            upper = c[i - 1][j] == '#' if 0 <= i - 1 else False
            lower = c[i + 1][j] == '#' if i + 1 < h else False
            left = c[i][j - 1] == '#' if 0 <= j - 1 else False
            right = c[i][j + 1] == '#' if j + 1 < w else False
            if not (upper or lower or left or right):
                ans = 'No'
                break
print(ans)
