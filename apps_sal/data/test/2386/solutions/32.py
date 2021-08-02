import statistics
from functools import reduce
n = int(input())
A = list(map(int, input().split()))
for i in range(n):
    A[i] -= i + 1

m = int(statistics.median(A))
ans1 = 0
ans2 = 0
for i in range(n):
    ans1 += abs(m - A[i])
    ans2 += abs(m + 1 - A[i])
print(min(ans1, ans2))
