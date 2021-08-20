(n, k) = map(int, input().split())
arr = [int(i) for i in input().split()]
total = 0
for i in range(n):
    total += arr[i] * min(n - k + 1, min(k, min(i, n - i - 1) + 1))
print('{0:.10f}'.format(total / (n - k + 1)))
