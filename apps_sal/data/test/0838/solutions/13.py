(n, m) = list(map(int, input().split()))
A = [0] * n
for i in range(n):
    A[i] = list(map(int, input().split()))
res = 0
for i in range(n):
    sum1 = sum(A[i])
    sum2 = m - sum1
    res += 2 ** sum1 + 2 ** sum2 - 2
sum1 = 0
sum2 = 0
for j in range(m):
    for i in range(n):
        sum1 += A[i][j]
    sum2 = n - sum1
    res += 2 ** sum1 + 2 ** sum2 - sum1 - sum2 - 2
    sum1 = 0
    sum2 = 0
print(res)
