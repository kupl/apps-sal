(n, k) = list(map(int, input().rstrip().split(' ')))
A = list(map(int, input().rstrip().split(' ')))
minValue = 100000
minIndex = -1
for i in range(n):
    if minValue > A[i]:
        minValue = A[i]
        minIndex = i
ans = (n - 2) // (k - 1) + 1
print(ans)
