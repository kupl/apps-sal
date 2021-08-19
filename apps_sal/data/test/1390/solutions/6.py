(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
minn = 10000000
for i in range(0, m - n + 1):
    if abs(A[n + i - 1] - A[i]) < minn:
        minn = A[n + i - 1] - A[i]
print(minn)
