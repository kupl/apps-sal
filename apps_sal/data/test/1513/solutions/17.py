(n, m, k) = map(int, input().split())
A = list(map(int, input().split()))
F = []
for i in range(1, n):
    F.append(A[i] - A[i - 1] - 1)
F.sort()
sum = 0
for i in range(0, n - k):
    sum += F[i]
print(sum + n)
