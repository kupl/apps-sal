h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
ans = [[0] * (w + 2) for i in range(h + 2)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i - 1][j - 1] == "#":
            ans[i - 1][j - 1] += 1
            ans[i - 1][j] += 1
            ans[i - 1][j + 1] += 1
            ans[i][j - 1] += 1
            ans[i][j + 1] += 1
            ans[i + 1][j - 1] += 1
            ans[i + 1][j] += 1
            ans[i + 1][j + 1] += 1

del ans[0]
del ans[-1]
for i in range(h):
    del ans[i][0]
    del ans[i][-1]
for i, _ in enumerate(s):
    tmp = ""
    for j, word in enumerate(_):
        if word == "#":
            tmp += "#"
        else:
            tmp += str(ans[i][j])
    print(tmp, end="\n")
