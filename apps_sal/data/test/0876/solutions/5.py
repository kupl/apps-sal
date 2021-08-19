def p(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr


def max_element(arr):
    x = 0
    for i in arr:
        x = max(x, i)
    return x


def kek(a, b):
    if (a <= b):
        return 1
    else:
        return 0


[n, k] = [int(x) for x in input().split()]


def matmul(m1, m2):
    s = 0  # сумма
    t = []  # временная матрица
    m3 = []  # конечная матрица
    if len(m2) != len(m1[0]):
        print("333")
    else:
        r1 = len(m1)  # количество строк в первой матрице
        c1 = len(m1[0])  # Количество столбцов в 1
        r2 = c1  # и строк во 2ой матрице
        c2 = len(m2[0])  # количество столбцов во 2ой матрице
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + m1[z][i] * m2[i][j]
                    s = min(s, k)
                t.append(s)
                s = 0
            m3.append(t)
            t = []
    return m3


def exp(m, p):
    if (p == 1):
        return m
    if (p % 2 == 0):
        w = exp(m, p // 2)
        return matmul(w, w)
    else:
        return matmul(m, exp(m, p - 1))


a = [int(x) for x in input().split()]
ind = 0
while a[ind] == 0:
    ind += 1
a = a[ind:]
n = len(a)
if (max_element(a) >= k):
    print(0)
else:
    a = [a]
    if (n >= 10):
        res = 0
        while(max_element(a[0]) < k):
            res += 1
            a[0] = p(a[0])
        print(res)
    elif n == 2:
        x1 = a[0][0]
        x2 = a[0][1]
        print((k - x2 + x1 - 1) // x1)
    else:
        m = []
        for i in range(n):
            m += [[kek(i, j) for j in range(n)]]
        l = 0
        r = 10**18
        while(l + 1 < r):
            mid = (l + r) // 2
            b = matmul(a, exp(m, mid))
            if max_element(b[0]) < k:
                l = mid
            else:
                r = mid
        print(r)
