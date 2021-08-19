def getn():
    return int(input())


def getns():
    return [int(x)for x in input().split()]


# n=getn()
# ns=getns()
n, m = getns()
a = [[0] * m for i in range(n)]
b = [[0] * m for i in range(n)]
a = []
b = []
for i in range(n):
    a.append(getns())
for i in range(n):
    b.append(getns())
for i in range(n):
    for j in range(m):
        a[i][j], b[i][j] = min(a[i][j], b[i][j]), max(a[i][j], b[i][j])


def check(x):
    for i in range(n):
        for j in range(m - 1):
            if x[i][j] >= x[i][j + 1]:
                return False
    for i in range(n - 1):
        for j in range(m):
            if x[i][j] >= x[i + 1][j]:
                return False
    return True


if check(a) and check(b):
    print('Possible')
else:
    print('Impossible')
quit()


print(a)
print(b)
