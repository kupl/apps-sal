import sys
(n, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
k = 0
m = M
i = 0
while i < n:
    while i < n and m >= A[i]:
        m -= A[i]
        i += 1
    else:
        k += 1
        m = M
print(k)
