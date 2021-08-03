h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            c = 0
            for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == "#":
                    c += 1
            if c == 0:
                print("No")
                return
print("Yes")
