import operator


def mx_or(mx):
    n = len(mx)
    m = len(mx[0])
    result = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if mx[i][j]:
                for k in range(n):
                    result[k][j] = 1
                for k in range(m):
                    result[i][k] = 1
    return result


def none(iterable):
    return all(map(operator.not_, iterable))


(n, m) = list(map(int, input().split()))
mx = [[] for i in range(n)]
for i in range(n):
    mx[i] = list(map(int, input().split()))
result = [[1 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if not mx[i][j]:
            for k in range(n):
                result[k][j] = 0
            for k in range(m):
                result[i][k] = 0
if mx_or(result) == mx:
    print('YES')
    for i in range(n):
        print(' '.join(map(str, result[i])))
else:
    print('NO')
