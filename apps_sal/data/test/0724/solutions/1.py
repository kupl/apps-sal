(n, d) = list(map(int, input().split()))
A = sorted([int(x) for x in input().split()])
result = n
for i in range(n):
    for j in range(i, n):
        if A[j] - A[i] <= d:
            result = min([result, i + n - j - 1])
print(result)
