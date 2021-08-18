from collections import defaultdict
n, m, k = list(map(int, input().split()))
a = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

total = n + m - 2
half = total // 2
b = defaultdict(dict)


def upper(i, j, val, cnt):
    val ^= a[i][j]
    if cnt == half:
        s = str(i) + ' ' + str(j)
        if val in b[s]:
            b[s][val] += 1
        else:
            b[s][val] = 1
        return
    if i + 1 < n:
        upper(i + 1, j, val, cnt + 1)
    if j + 1 < m:
        upper(i, j + 1, val, cnt + 1)


answer = 0


def lower(i, j, val, cnt):
    nonlocal answer
    s = str(i) + ' ' + str(j)
    if cnt == total - half:
        aim = k ^ val
        if aim in b[s]:
            answer += b[s][aim]
        return
    if i > 0:
        lower(i - 1, j, val ^ a[i][j], cnt + 1)
    if j > 0:
        lower(i, j - 1, val ^ a[i][j], cnt + 1)


upper(0, 0, 0, 0)
lower(n - 1, m - 1, 0, 0)

print(answer)
