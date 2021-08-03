N = int(input())

A = list(map(int, input().split()))
A.sort()
divide = len(A) // 2

ans = A[divide] - A[divide - 1]
print(ans)
