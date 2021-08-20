from collections import Counter


def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


n = read()
X = []
Y = []
for _ in range(n):
    (x, y) = readmap()
    X.append(x)
    Y.append(y)
A = []
B = []
for _ in range(n):
    (a, b) = readmap()
    A.append(a)
    B.append(b)
c = Counter()
for i in range(n):
    for j in range(n):
        coordinate = (X[i] + A[j], Y[i] + B[j])
        c[coordinate] += 1
for (k, v) in c.items():
    if v >= n:
        print(k[0], k[1])
