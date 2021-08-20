[n, m] = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
x = int(input())
for i in range(1, n + 1):
    a[i] += a[i - 1]
for i in range(1, m + 1):
    b[i] += b[i - 1]
INF = 4 * 10 ** 9 + 1
A = [INF] * (n + 1)
B = [INF] * (m + 1)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        A[i - j + 1] = min(A[i - j + 1], a[i] - a[j - 1])
for i in range(1, m + 1):
    for j in range(1, i + 1):
        B[i - j + 1] = min(B[i - j + 1], b[i] - b[j - 1])
answ = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i] * B[j] <= x:
            answ = max(answ, i * j)
print(answ)
