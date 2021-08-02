A = list(map(int, input().split()))
A.sort()
ans = A[1] - A[0] + A[2] - A[1]
print(ans)
