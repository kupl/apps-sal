n, m = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
MIN = 1000000000
for i in range(m - n + 1):
    MIN = min(A[i + n - 1] - A[i], MIN)
print(MIN)
