n, n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
if n1 > n2:
    n2, n1 = n1, n2
A.sort()
sums1 = 0
sums2 = 0
for j in range(n - 1, n - 1 - n1, -1):
    sums1 += A[j]
for j in range(n - 1 - n1, n - 1 - n1 - n2, -1):
    sums2 += A[j]
print(sums1 / n1 + sums2 / n2)
