# coding:utf-8
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = [[0] * w for _ in range(h)]
x = [-1, 0, 1, -1, 1, -1, 0, 1]
y = [-1, -1, -1, 0, 0, 1, 1, 1]

# print(s)


for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] = '#'
        else:
            for k in range(len(x)):
                if 0 <= (i + x[k]) < h and 0 <= (j + y[k]) < w and s[i + x[k]][j + y[k]] == '#':
                    ans[i][j] += 1

for i in range(h):
    print(*ans[i], sep='')
