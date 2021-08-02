n, m = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
A = [0] * (n + 1)
B = [0] * (m + 1)

x = int(input())

for i in range(1, n + 1):
    a[i] = a[i - 1] + a[i]
    A[i] = a[i]
    for j in range(1, i):
        A[i - j] = min(A[i - j], a[i] - a[j])

for i in range(1, m + 1):
    b[i] = b[i - 1] + b[i]
    B[i] = b[i]
    for j in range(1, i):
        B[i - j] = min(B[i - j], b[i] - b[j])

res = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i] * B[j] <= x:
            res = max(res, i * j)
print(res)
