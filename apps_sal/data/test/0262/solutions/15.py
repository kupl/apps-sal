
n = int(input())

v = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(1)
    return


def sum_diag1(v):
    s = 0
    for i in range(len(v)):
        s += v[i][i]
    return s


def sum_diag2(v):
    s = 0
    for i in range(len(v)):
        s += v[i][len(v) - 1 - i]
    return s


def sum_row(v, r):
    return sum(v[r])


def sum_col(v, c):
    s = 0
    for r in range(len(v)):
        s += v[r][c]
    return s


row = 0
col = 0

needed_sum = 0
row_sum = 0
col_sum = 0
diag1_sum = 0
diag2_sum = 0

for r in range(len(v)):
    if 0 in v[r]:
        row = r
        col = v[r].index(0)
        if needed_sum != 0:
            break
    elif needed_sum == 0:
        needed_sum = sum(v[r])

t = needed_sum - sum(v[row])
v[row][col] = t

l = [sum_row(v, r) for r in range(n)]
l += [sum_col(v, c) for c in range(n)]
l += [sum_diag1(v), sum_diag2(v)]

if len(set(l)) == 1 and t > 0:
    print(t)
else:
    print(-1)
