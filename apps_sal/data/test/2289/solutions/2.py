from bisect import bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
K = list(map(int, input().split()))

for i in range(1, N):
    A[i] += A[i-1]

ans = []
plus = 0
for q in range(Q):
    idx = bisect_right(A, K[q]+plus)
    if idx == N:
        ans.append(N)
        plus = 0
    else:
        ans.append(N-idx)
        plus += K[q]

for q in range(Q):
    print(ans[q])
