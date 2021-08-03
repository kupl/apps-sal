import math

n = int(input())
A = [int(i) for i in input().split()]
A.sort()

ans = 10**18
val = 0
for mid in range(1, 100):
    cost = 0
    for i in range(n):
        cost += min(abs(A[i] - mid), abs(A[i] - mid + 1), abs(A[i] - mid - 1))
    if cost < ans:
        ans = cost
        val = mid

print(val, ans)
