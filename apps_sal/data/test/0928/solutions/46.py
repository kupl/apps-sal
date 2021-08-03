from bisect import bisect_right, bisect_left
N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
prev = 0
for i in range(1, len(A)):
    A[i] = A[i] + A[i - 1]

ans = 0
for i in range(len(A)):
    if A[i] >= K:
        ans += bisect_right(A, A[i] - K)
print(ans)
