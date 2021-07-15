import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = max(A)

while right - left > 1:
    mid = (left + right) // 2
    jk = 0
    for i in range(N):
        jk += A[i] // mid - 1
        if A[i] % mid != 0: jk += 1
    if jk <= K:
        right = mid
    else:
        left = mid

print(right)
