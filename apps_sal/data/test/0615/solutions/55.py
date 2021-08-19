from itertools import accumulate
N = int(input())
A = list(map(int, input().split()))
X = list(accumulate(A))
l = 0
L = [-1] * N
for m in range(2, N - 1):
    target = X[m - 1] / 2
    while l + 1 <= m and abs(target - X[l]) >= abs(target - X[l + 1]):
        l += 1
    L[m] = l
r = N - 1
r_sum = 0
R = [-1] * N
for m in reversed(list(range(2, N - 1))):
    target = (X[-1] - X[m - 1]) / 2
    while r - 1 >= m and abs(target - r_sum) >= abs(target - (r_sum + A[r])):
        r_sum += A[r]
        r -= 1
    R[m] = r
ans = float('inf')
for m in range(2, N - 1):
    (li, ri) = (L[m], R[m])
    (B, C, D, E) = (X[li], X[m - 1] - X[li], X[ri] - X[m - 1], X[-1] - X[ri])
    ans = min(ans, max(B, C, D, E) - min(B, C, D, E))
print(ans)
