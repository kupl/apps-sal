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


n = int(input())
p = getIntList()
p.sort()
result1 = 0
for (i, x) in enumerate(p):
    result1 += abs(x - (2 * i + 1))
result2 = 0
for (i, x) in enumerate(p):
    result2 += abs(x - (2 * i + 2))
print(min(result1, result2))
