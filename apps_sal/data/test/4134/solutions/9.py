n, m, k = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
re = 0
half = (m + n - 2) // 2
d = [dict() for _ in range(22)]


def forward(i, j, value):
    if i >= n or j >= m:
        return
    value ^= l[i][j]
    if i + j == half:
        if value in d[i]:
            d[i][value] += 1
        else:
            d[i][value] = 1
        return None
    forward(i + 1, j, value)
    forward(i, j + 1, value)


def backward(i, j, value):
    if i < 0 or j < 0:
        return
    if i + j == half:
        tmp = k ^ value
        # print(tmp)
        if tmp in d[i]:
            nonlocal re
            re += d[i][tmp]
        return None
    value ^= l[i][j]
    backward(i - 1, j, value)
    backward(i, j - 1, value)


forward(0, 0, 0)
backward(n - 1, m - 1, 0)
# print(d)
print(re)
