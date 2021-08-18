r, c = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(r)]
# print(s)
re = 0
for i in range(r - 1, -1, -1):
    for j in range(c - 1, -1, -1):
        if 0 < i < r - 1 and 0 < j < c - 1:
            if s[i][j] == 0:
                s[i][j] = min(s[i + 1][j], s[i][j + 1]) - 1
            if (s[i - 1][j] > 0 and s[i - 1][j] >= s[i][j]) or (s[i][j - 1] > 0 and s[i][j - 1] >= s[i][j]):
                print(-1)
                return
        if i < r - 1 and j < c - 1:
            if s[i][j] >= s[i + 1][j] or s[i][j] >= s[i][j + 1]:
                print(-1)
                return
        if i < r - 1 and j == c - 1:
            if s[i][j] >= s[i + 1][j]:
                print(-1)
                return
        if i == r - 1 and j < c - 1:
            if s[i][j] >= s[i][j + 1]:
                print(-1)
                return
        re += s[i][j]
print(re)
