n, m = list(map(int, input().split()))
grid = [list(input()) for i in range(n)]
cnt = 0
for r in range(n-1):
    for c in range(m-1):
        face = ['f', 'a', 'c', 'e']
        if grid[r][c] in face:
            face.remove(grid[r][c])
            if grid[r+1][c] in face:
                face.remove(grid[r+1][c])
                if grid[r][c+1] in face:
                    face.remove(grid[r][c+1])
                    if grid[r+1][c+1] in face:
                        face.remove(grid[r+1][c+1])
                        cnt += 1
print(cnt)

