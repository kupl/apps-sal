__author__ = 'Andrey'


def retest(row):
    nonlocal table
    row_n = table[row]
    m_ax = 0
    curr = 0
    for item in row_n:
        if item == 1:
            curr += 1
        if item == 0:
            m_ax = max(curr, m_ax)
            curr = 0
    m_ax = max(curr, m_ax)
    return m_ax


n, m, q = list(map(int, input().split()))
table = []
for x in range(n):
    table.append(list(map(int, input().split())))
maximums = []
for y in range(n):
    maximums.append(retest(y))
for z in range(q):
    i, j = list(map(int, input().split()))
    table[i - 1][j - 1] = 1 - table[i - 1][j - 1]
    maximums[i - 1] = retest(i - 1)
    print(max(maximums))
