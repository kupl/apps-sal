n, m = list(map(int, input().split()))
MAP = [list(input()) for i in range(n)]

ANSMAP = [["." for i in range(m)] for j in range(n)]

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if MAP[i - 1][j - 1] == "#" and MAP[i - 1][j] == "#" and MAP[i - 1][j + 1] == "#" and MAP[i][j - 1] == "#" and MAP[i - 1][j + 1] == "#" and MAP[i + 1][j - 1] == "#" and MAP[i + 1][j] == "#" and MAP[i + 1][j + 1] == "#":
            ANSMAP[i - 1][j - 1] = "#"
            ANSMAP[i - 1][j] = "#"
            ANSMAP[i - 1][j + 1] = "#"
            ANSMAP[i][j - 1] = "#"
            ANSMAP[i][j + 1] = "#"
            ANSMAP[i + 1][j - 1] = "#"
            ANSMAP[i + 1][j] = "#"
            ANSMAP[i + 1][j + 1] = "#"

if MAP == ANSMAP:
    print("YES")

else:
    print("NO")
