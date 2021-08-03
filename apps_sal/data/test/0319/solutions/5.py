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


n, m = getIntList()
a = []
for _ in range(n):
    s = input()
    a.append([int(s[i]) for i in range(m)])
sumA = [0] * m
for i in range(n):
    for j in range(m):
        sumA[j] += a[i][j]


def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and sumA[j] == 1:
                break
        else:
            return "YES"
    return "NO"


print(check())
