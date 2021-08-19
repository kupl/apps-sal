def R():
    return list(map(int, input().split()))


def G():
    return map(int, input().split())


(n, a, b) = G()
A = R()
B = R()
result = [-1 for i in range(n + 1)]
for i in range(a):
    result[A[i]] = 1
for i in range(1, n + 1):
    if result[i] == -1:
        result[i] = 2
for i in range(1, n + 1):
    print(result[i], end=' ')
