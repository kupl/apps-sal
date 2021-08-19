import sys
A = list(map(int, input().split()))
A.sort()
A.reverse()
ans = abs(A[1] - A[0]) + abs(A[2] - A[1])
print(ans)
