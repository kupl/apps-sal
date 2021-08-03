import math


def getIntList():
    return list(map(int, input().split()))


def getTransIntList(n):
    first = getIntList()
    m = len(first)
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        result[i][0] = first[i]
    for j in range(1, n):
        curr = getIntList()
        for i in range(m):
            result[i][j] = curr[i]
    return result


n, a, b = getIntList()
if a > 1 and b > 1:
    print('NO')
elif a == b == 1 and (n == 2 or n == 3):
    print('NO')
else:
    c = max(a, b)
    m = [[0] * n for _ in range(n)]
    for i in range(n - c):
        m[i][i + 1] = 1
        m[i + 1][i] = 1
    if b > 1:
        for i in range(n):
            for j in range(n):
                if i != j:
                    m[i][j] = 1 - m[i][j]
    print('YES')
    for i in range(n):
        print(''.join(map(str, m[i])))
